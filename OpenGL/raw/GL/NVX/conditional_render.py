'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NVX_conditional_render'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NVX_conditional_render',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLuint)
def glBeginConditionalRenderNVX(id):pass
@_f
@_p.types(None,)
def glEndConditionalRenderNVX():pass