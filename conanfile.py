#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class PremakeInstallerConan(ConanFile):
    name = "premake_installer"
    version = "4.3"
    description = "Premake is a command line utility which reads a scripted definition of a software project and, " \
                  "most commonly, uses it to generate project files for toolsets like Visual Studio, Xcode, or GNU Make"
    url = "https://github.com/bincrafters/conan-premake_installer"
    homepage = "https://premake.github.io"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD"
    exports = ["LICENSE.md"]
    settings = 'os_build'

    def configure(self):
        if not self.settings.os_build in ["Windows", "Linux", "Macos"]:
            raise Exception("Only Windows, Linux and macOS are supported")

    def source(self):
        if self.settings.os_build == "Windows":
            zip_name = "windows.zip"
            zip_sha256 = "f2e9c2d7b33e06b51dc2d0a9d4d1d398e4debad0d8254e17a031b04f57da4d67"
        elif self.settings.os_build == "Linux":
            zip_name = "linux.tar.gz"
            zip_sha256 = "41783914f792e10a34ebf0fd4bd14a10a53c18047e5b58d782c822804eb7703b"
        elif self.settings.os_build == "Macos":
            zip_name = "macosx.tar.gz"
            zip_sha256 = "a6b89b3d2891c45637e87aa75311d9c04fe79d6b2aac5e2ab24a746b8178aceb"
        source_url = "http://sourceforge.net/projects/premake/files/Premake/4.3/premake-{}-{}/download".format(self.version, zip_name)
        tools.get(source_url, sha256=zip_sha256)
        # os.rename('premake-core-%s' % self.version, self._source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy(pattern="*premake4.exe", dst="bin", keep_path=False)
        self.copy(pattern="*premake4", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))
