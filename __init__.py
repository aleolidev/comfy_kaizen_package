"""Kaizen Package - ComfyUI Custom Nodes for Image Processing."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """Alejandro Olivares"""
__email__ = "codekaizendev@gmail.com"
__version__ = "0.0.1"

# Import from the correct location for ComfyUI
try:
    from .src.kaizen_package.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    # Fallback for development or alternative structures
    try:
        from src.kaizen_package.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        print("Warning: Could not import kaizen_package nodes")
        NODE_CLASS_MAPPINGS = {}
        NODE_DISPLAY_NAME_MAPPINGS = {}

# Make sure the mappings are available at the package level
__all__.extend(["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"])


