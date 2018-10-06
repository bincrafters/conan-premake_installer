#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class PremakeInstallerConan(ConanFile):
    name = "premake_installer"
    version = "5.0.0-alpha12"
    description = "Premake is a command line utility which reads a scripted definition of a software project and, " \
                  "most commonly, uses it to generate project files for toolsets like Visual Studio, Xcode, or GNU Make"
    url = "https://github.com/bincrafters/conan-premake_installer"
    homepage = "https://premake.github.io/"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD"
    exports = ["LICENSE.md"]
    settings = 'os_build', 'arch_build', 'compiler'
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/premake/premake-core/archive/v{version}.tar.gz".format(version=self.version)
        tools.get(source_url)
        os.rename('premake-core-%s' % self.version, self.source_subfolder)

    def build(self):
        with tools.chdir(self.source_subfolder):
            if self.settings.os_build == 'Windows':
                with tools.vcvars(self.settings):
                    self.run('nmake -f Bootstrap.mak windows')
            elif self.settings.os_build == 'Linux':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['-f', 'Bootstrap.mak', 'linux'])
            elif self.settings.os_build == 'Macos':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['-f', 'Bootstrap.mak', 'osx'])

    def package(self):
        self.copy(pattern="*premake5.exe", dst="bin", keep_path=False)
        self.copy(pattern="*premake5", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))

    def package_id(self):
        self.info.settings.compiler = 'Any'
