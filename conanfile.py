#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tempfile
from conans import ConanFile, tools, AutoToolsBuildEnvironment


class PremakeInstallerConan(ConanFile):
    name = "premake_installer"
    version = "4.4-beta3"
    description = "Premake is a command line utility which reads a scripted definition of a software project and, " \
                  "most commonly, uses it to generate project files for toolsets like Visual Studio, Xcode, or GNU Make"
    url = "https://github.com/bincrafters/conan-premake_installer"
    homepage = "https://github.com/premake/premake-core"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD-3-Clause"
    exports = ["LICENSE.md"]
    settings = 'os_build', 'arch_build', 'compiler'
    _source_subfolder = "source_subfolder"
    _install_subfolder = tempfile.mkdtemp()

    def source(self):
        source_url = "{}/archive/{}.tar.gz".format(self.homepage, self.version)
        tools.get(source_url, sha256="2a31d46f6fed1e1322747b9d8683be8db78258a3281c4a8f0a95cc51b303be14")
        os.rename('premake-core-%s' % self.version, self._source_subfolder)

    def build(self):
        with tools.chdir(os.path.join(self._source_subfolder, "src", "host", "lua-5.1.4")):
            tools.replace_in_file("Makefile", "/usr/local", self._install_subfolder)
            if self.settings.os_build == 'Windows':
                with tools.vcvars(self.settings):
                    self.run('nmake -f Makefile windows')
                    self.run('nmake install')
            elif self.settings.os_build == 'Linux':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['-f', 'Makefile', 'linux'])
                env_build.install()
            elif self.settings.os_build == 'Macos':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['-f', 'Makefile', 'osx'])
                env_build.install()

    def package(self):
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder)
        suffix = ".exe" if self.settings.os_build == "Windows" else ""
        self.copy(pattern="premake4{}".format(suffix), dst="bin", src=os.path.join(self._install_subfolder, "bin"))

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))

    def package_id(self):
        self.info.settings.compiler = 'Any'
