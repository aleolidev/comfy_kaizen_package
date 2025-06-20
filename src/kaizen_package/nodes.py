"""Kaizen Package - ComfyUI Custom Nodes for Image Processing."""

import torch
import torch.nn.functional as F


class ImageComposite:
    """
    Composite images using mask-based alpha blending with precise positioning.

    Overlays a source image onto a background at specified coordinates using a mask
    to control transparency. Supports negative positioning and automatic size matching.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "background": ("IMAGE", {"tooltip": "Background image"}),
                "foreground": ("IMAGE", {"tooltip": "Image to overlay"}),
                "mask": ("MASK", {"tooltip": "Alpha mask (1.0=opaque, 0.0=transparent)"}),
                "x": ("INT", {
                    "default": 0, "min": -4096, "max": 4096, "step": 1,
                    "tooltip": "Horizontal position (negative values supported)"
                }),
                "y": ("INT", {
                    "default": 0, "min": -4096, "max": 4096, "step": 1,
                    "tooltip": "Vertical position (negative values supported)"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("composite",)
    FUNCTION = "compose"
    CATEGORY = "kaizen/image"

    def compose(self, background, foreground, mask, x, y):
        """Composite foreground onto background using mask-based alpha blending."""
        # Extract first batch items
        bg = background[0]
        fg = foreground[0]
        mask_tensor = mask[0]

        # Normalize mask to [H, W, 3] format
        mask_tensor = self._prepare_mask(mask_tensor, fg.shape[:2])

        # Apply mask to foreground
        masked_fg = fg * mask_tensor

        # Perform compositing
        result = self._composite_images(bg, masked_fg, mask_tensor, x, y)

        return (result.unsqueeze(0),)

    def _prepare_mask(self, mask, target_size):
        """Prepare mask to match foreground image dimensions."""
        # Add channel dimension if needed
        if len(mask.shape) == 2:
            mask = mask.unsqueeze(-1)

        # Expand to 3 channels
        if mask.shape[-1] == 1:
            mask = mask.repeat(1, 1, 3)

        # Resize if dimensions don't match
        if mask.shape[:2] != target_size:
            mask = F.interpolate(
                mask.permute(2, 0, 1).unsqueeze(0),
                size=target_size,
                mode='bilinear',
                align_corners=False
            ).squeeze(0).permute(1, 2, 0)

        return mask

    def _composite_images(self, background, masked_foreground, mask, x, y):
        """Perform the actual image compositing with bounds checking."""
        bg_h, bg_w = background.shape[:2]
        fg_h, fg_w = masked_foreground.shape[:2]

        result = background.clone()

        # Calculate valid regions
        start_x = max(0, x)
        start_y = max(0, y)
        end_x = min(bg_w, x + fg_w)
        end_y = min(bg_h, y + fg_h)

        src_start_x = max(0, -x)
        src_start_y = max(0, -y)
        src_end_x = src_start_x + (end_x - start_x)
        src_end_y = src_start_y + (end_y - start_y)

        # Composite if regions overlap
        if start_x < end_x and start_y < end_y:
            bg_region = result[start_y:end_y, start_x:end_x]
            fg_region = masked_foreground[src_start_y:src_end_y, src_start_x:src_end_x]
            mask_region = mask[src_start_y:src_end_y, src_start_x:src_end_x]

            # Alpha blend: fg * alpha + bg * (1 - alpha)
            result[start_y:end_y, start_x:end_x] = fg_region + bg_region * (1 - mask_region)

        return result


# Node registration
NODE_CLASS_MAPPINGS = {
    "KaizenImageComposite": ImageComposite,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KaizenImageComposite": "Image Composite",
}
