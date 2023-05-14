from sanic import Request, Sanic, json

app = Sanic("TestApp")


@app.get("/")
async def handler(request: Request):
    return json({"foo": "bar"})
