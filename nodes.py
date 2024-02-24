import comfy
from comfy_extras.nodes_upscale_model import ImageUpscaleWithModel

class UpscaleImageByUsingModel:
    rescale_methods = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]
     
    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "upscale"
    CATEGORY = "image/upscaling"
    
    def __init__(self):
        self.__imageScaler = ImageUpscaleWithModel()
    
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "upscale_model": ("UPSCALE_MODEL",),
                "image": ("IMAGE",),
                "upscale_by": ("FLOAT", {
                    "default": 2.0,
                    "min": 1.0,
                    "max": 8.0,
                    "step": 0.05,
                }),
                "rescale_method": (self.rescale_methods,),
            }
        }
        
    def upscale(self, upscale_model, image, upscale_by, rescale_method):
        samples = image.movedim(-1,1)

        width = round(samples.shape[3])
        height = round(samples.shape[2])

        target_width = round(samples.shape[3] * upscale_by)
        target_height = round(samples.shape[2] * upscale_by)

        samples = self.__imageScaler.upscale(upscale_model, image)[0].movedim(-1,1)

        upscaled_width = round(samples.shape[3])
        upscaled_height = round(samples.shape[2])

        if upscaled_width > target_width or upscaled_height > target_height:
            samples = comfy.utils.common_upscale(samples, target_width, target_height, rescale_method, "disabled")
            
        samples = samples.movedim(1,-1)
        return (samples,)
