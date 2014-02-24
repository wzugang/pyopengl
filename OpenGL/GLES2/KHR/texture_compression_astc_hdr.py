'''OpenGL extension KHR.texture_compression_astc_hdr

This module customises the behaviour of the 
OpenGL.raw.GLES2.KHR.texture_compression_astc_hdr to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/texture_compression_astc_hdr.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.KHR.texture_compression_astc_hdr import *
from OpenGL.raw.GLES2.KHR.texture_compression_astc_hdr import _EXTENSION_NAME

def glInitTextureCompressionAstcHdrKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION