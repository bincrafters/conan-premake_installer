from conans import ConanFile, tools, AutoToolsBuildEnvironment, MSBuild
import os


class PremakeInstallerConan(ConanFile):
    name = "premake_installer"
    version = "5.0.0-alpha14"
    description = "Premake is a command line utility which reads a scripted definition of a software project and, " \
                  "most commonly, uses it to generate project files for toolsets like Visual Studio, Xcode, or GNU Make"
    url = "https://github.com/bincrafters/conan-premake_installer"
    homepage = "https://premake.github.io/"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD"
    exports = ["LICENSE.md"]
    settings = 'os_build', 'arch_build', 'compiler'
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/premake/premake-core/releases/download/v{version}/premake-{version}-src.zip".format(version=self.version)
        tools.get(source_url, sha256="7c9fa4488156625c819dd03f2b48bfd4712fbfabdc2b5768e8c7f52dd7d16608")
        os.rename('premake-%s' % self.version, self._source_subfolder)

    @property
    def _platform(self):
        return {'Windows': 'vs2017',
                'Linux': 'gmake.unix',
                'Macos': 'gmake.macosx'}.get(str(self.settings.os_build))

    def build(self):
        with tools.chdir(os.path.join(self._source_subfolder, 'build', self._platform)):
            if self.settings.os_build == 'Windows':
                msbuild = MSBuild(self)
                msbuild.build("Premake5.sln", platforms={'x86': 'Win32', 'x86_64': 'x64'}, build_type="Release", arch=self.settings.arch_build)
            elif self.settings.os_build == 'Linux':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['config=release'])
            elif self.settings.os_build == 'Macos':
                env_build = AutoToolsBuildEnvironment(self)
                env_build.make(args=['config=release'])

    def package(self):
        self.copy(pattern="*premake5.exe", dst="bin", keep_path=False)
        self.copy(pattern="*premake5", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))

    def package_id(self):
        self.info.settings.compiler = 'Any'
