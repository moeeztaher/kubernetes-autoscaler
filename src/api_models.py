from litestar.datastructures import UploadFile
from pydantic import BaseConfig, BaseModel


class FormData(BaseModel):
    """Form data model."""

    image: UploadFile
    filename: str

    class Config(BaseConfig):
        """Pydantic configuration."""

        arbitrary_types_allowed = True
