import time

from fastapi import FastAPI, Form
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send
from transformers import pipeline

app = FastAPI(debug=True)
# Prepare model in local folder:
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# summarizer.save_pretrained("./model")

# facebook/bart-large-cnn
summarizer = pipeline("summarization", model="./model")


@app.post("/v1/summarize/")
def create_item(text: str = Form(), min_length: int = Form(default=30), max_length: int = Form(default=130)):
    _max_length = min(max_length, len(text))
    return summarizer(text, max_length=_max_length, min_length=min_length, do_sample=False)


class STARLETTEProcessTimeMiddleware:
    app: ASGIApp

    def __init__(self, app: ASGIApp, ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        start_time = time.time()

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(round(time.time() - start_time, 4)))
            await send(message)

        await self.app(scope, receive, send_wrapper)


app.add_middleware(STARLETTEProcessTimeMiddleware)
