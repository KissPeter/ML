import time

from fastapi import FastAPI, Form
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send
from transformers import pipeline

app = FastAPI(debug=True)
# Prepare model in local folder:
# summarizer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
# summarizer.save_pretrained("./model")

# cardiffnlp/twitter-roberta-base-sentiment-latest
model_path = "model"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


@app.post("/v1/score/")
def create_item(text: str = Form(), ):
    return sentiment_task(text)


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
