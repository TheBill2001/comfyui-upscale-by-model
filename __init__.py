"""
@author: Trần Nam Tuấn
@title: Upscale Image By (Using Model)
@nickname: Upscale Image By (Using Model)
@description: This custom node allow upscaling an image by a factor using a model.
"""

from .nodes import *

NODE_CLASS_MAPPINGS = {
    "UpscaleImageByUsingModel": UpscaleImageByUsingModel
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UpscaleImageByUsingModel": "Upscale Image By (Using Model)"
}
