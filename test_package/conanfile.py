#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        self.run('premake4 --version || echo "ignore premake4 exit code"', run_environment=True)
