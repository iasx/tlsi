import falcon
import falcon.asgi
from model import Model
from falcon import CORSMiddleware, HTTPInternalServerError


class MainResource:
    """Health check endpoint"""

    def __init__(self, model):
        self.model = model

    async def on_options(self, i, o):
        o.content_type = falcon.MEDIA_TEXT
        o.status = falcon.HTTP_200
        o.text = "OK"

    async def on_get(self, i, o):
        o.content_type = falcon.MEDIA_TEXT
        o.status = falcon.HTTP_200
        o.text = "Alive!"

    async def on_post(self, i, o):
        try:
            o.text = self.model((await i.media)["text"])
            o.content_type = falcon.MEDIA_TEXT
            o.status = falcon.HTTP_200
        except Exception as no:
            raise HTTPInternalServerError("Internal Server Error", str(no))


app = falcon.asgi.App(
    cors_enable=True,
    middleware=[
        # TODO: AuthMiddleware(),
        CORSMiddleware(
            allow_origins="*",
            allow_credentials="*",
        ),
    ],
)

model = Model()

app.add_route("/", MainResource(model))
