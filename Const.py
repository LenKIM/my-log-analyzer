# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import sys


class _const:
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        a = self.__dict__
        if a in name:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value


sys.modules[__name__] = _const()
