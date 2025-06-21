"""
Kaizen Package - ComfyUI Custom Nodes
Entry point for ComfyUI node registration
"""

# Import the actual node implementations
try:
    from .src.kaizen_package.nodes import (
        ImageComposite,
        NODE_CLASS_MAPPINGS as _NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as _NODE_DISPLAY_NAME_MAPPINGS
    )
except ImportError:
    try:
        from src.kaizen_package.nodes import (
            ImageComposite,
            NODE_CLASS_MAPPINGS as _NODE_CLASS_MAPPINGS,
            NODE_DISPLAY_NAME_MAPPINGS as _NODE_DISPLAY_NAME_MAPPINGS
        )
    except ImportError:
        print("Error: Could not import kaizen_package nodes")
        _NODE_CLASS_MAPPINGS = {}
        _NODE_DISPLAY_NAME_MAPPINGS = {}

# Export the mappings that ComfyUI expects to find
NODE_CLASS_MAPPINGS = _NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = _NODE_DISPLAY_NAME_MAPPINGS

# Optional: Add version info for debugging
WEB_DIRECTORY = "./web"
__version__ = "0.0.1"
