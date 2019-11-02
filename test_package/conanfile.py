from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        self.run("premake5 --version", run_environment=True)
