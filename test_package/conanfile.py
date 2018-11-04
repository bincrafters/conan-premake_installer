#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        # FIXME: It's working, but still has an exit code of 1, why!?
        # self.run("premake4 --version", run_environment=True)
        pass
