from sanic import Request, Sanic, json

app = Sanic("TestApp")


@app.get("/<path:path>")
async def handler(request: Request, path):
    return json({"foo": "bar"})
