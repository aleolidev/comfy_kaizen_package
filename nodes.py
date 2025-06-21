"""
Kaizen Package - ComfyUI Custom Nodes
Entry point for ComfyUI node registration
"""

# Import the actual node implementations from the new structure
try:
    # Try relative import first (when used as part of a package)
    from .modules.kaizen.image_ops import (
        ImageComposite,
        NODE_CLASS_MAPPINGS as _NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as _NODE_DISPLAY_NAME_MAPPINGS
    )
except ImportError:
    # Fallback to absolute import (when used directly)
    from modules.kaizen.image_ops import (
        ImageComposite,
        NODE_CLASS_MAPPINGS as _NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as _NODE_DISPLAY_NAME_MAPPINGS
    )

# Export the mappings that ComfyUI expects to find
NODE_CLASS_MAPPINGS = _NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = _NODE_DISPLAY_NAME_MAPPINGS

# Optional: Add version info for debugging
WEB_DIRECTORY = "./web"
__version__ = "0.0.1"
