from typing import Annotated

from litestar import Litestar, get, post
from litestar.enums import MediaType, RequestEncodingType
from litestar.params import Body
from litestar.status_codes import HTTP_200_OK
from msgspec.json import encode

from src.api_models import FormData
from src.resnet_model import ResnetClassifier
from src.utils import load_img_from_bytes


@get("/")
async def index() -> str:
    """Returns the index page."""
    return "Welcome to the Elastic ML Inference API."


@post("/predict", media_type=MediaType.JSON, status_code=HTTP_200_OK)
async def predict(
    data: Annotated[FormData, Body(media_type=RequestEncodingType.MULTI_PART)], results: int = 5
) -> bytes:
    """Returns the predictions for the input image."""
    content = await data.image.read()
    input_img = load_img_from_bytes(content)
    return encode(ResnetClassifier.get_or_create_instance().predict(img=input_img, n_results=results))


app = Litestar([index, predict])
