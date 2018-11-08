#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, MSBuild, AutoToolsBuildEnvironment
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
    settings = {"os_build": ["Windows", "Linux", "Macos"],
                "arch_build": ["x86", "x86_64"]}
    _source_subfolder = 'sources'

    def source(self):
        source_url = "http://sourceforge.net/projects/premake/files/Premake/{version}/premake-{version}-src.zip".format(
            version=self.version)
        tools.get(source_url, sha256="36536490f8928d8ecde135da80cd8b751ea5bebe50cabba5c0de49cd41cb2780")
        os.rename('premake-%s' % self.version, self._source_subfolder)

    def _build_msvc(self):
        with tools.chdir(os.path.join(self._source_subfolder, 'build', 'vs2010')):

            if self.settings.arch_build == "x86_64":
                tools.replace_in_file('Premake4.sln', 'Win32', 'x64')
                tools.replace_in_file('Premake4.vcxproj', 'Win32', 'x64')
                tools.replace_in_file('Premake4.vcxproj', 'MachineX86', 'MachineX64')

            with tools.vcvars(self.settings, arch=str(self.settings.arch_build), force=True):
                msbuild = MSBuild(self)
                msbuild.build('Premake4.sln', build_type='Release', arch=self.settings.arch_build,
                              platforms={'x86': 'Win32'})

    def _build_make(self):
        make = "gmake.macosx" if self.settings.os == "Macos" else "gmake.unix"
        with tools.chdir(os.path.join(self._source_subfolder, 'build', make)):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make(args=['config=release'])

    def build(self):
        if self.settings.os_build == "Windows":
            self._build_msvc()
        else:
            self._build_make()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*premake4.exe", dst="bin", keep_path=False)
        self.copy(pattern="*premake4", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))
