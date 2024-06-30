from io import BytesIO
from pathlib import Path

from PIL.Image import Image
from PIL.Image import open as pil_open


def load_img_from_path(file_path: Path) -> Image:
    """Loads an image from a file path."""
    with open(file_path, "rb+") as f:
        img = pil_open(f)
        # TODO: fix type hinting for load method
        img.load()  # type: ignore
    return img


def load_img_from_bytes(img_bytes: bytes) -> Image:
    """Loads an image from a byte stream."""
    img_buffer = BytesIO(img_bytes)
    img = pil_open(img_buffer)
    # TODO: fix type hinting for load method
    img.load()  # type: ignore
    return img
