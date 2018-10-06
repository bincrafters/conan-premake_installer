[![Download](https://api.bintray.com/packages/bincrafters/public-conan/premake_installer%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/premake_installer%3Abincrafters/_latestVersion)
[![Build Status](https://travis-ci.org/bincrafters/conan-premake_installer.svg?branch=testing%2F5.0.0-alpha12)](https://travis-ci.org/bincrafters/conan-premake_installer)
[![Build status](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-premake_installer?branch=testing%2F5.0.0-alpha12&svg=true)](https://ci.appveyor.com/project/bincrafters/conan-premake_installer)

[Conan.io](https://conan.io) package recipe for [*premake_installer*](https://premake.github.io/).

Keep it short

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/bincrafters/public-conan/premake_installer%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install premake_installer/5.0.0-alpha12@bincrafters/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    premake_installer/5.0.0-alpha12@bincrafters/testing

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create bincrafters/testing



## Add Remote

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload premake_installer/5.0.0-alpha12@bincrafters/testing --all -r bincrafters


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package premake_installer.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](git@github.com:bincrafters/conan-premake_installer.git/blob/testing/5.0.0-alpha12/LICENSE.md)
