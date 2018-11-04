#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        self.run("premake4 --version", run_environment=True)
