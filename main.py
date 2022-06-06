from fastapi import FastAPI

app = FastAPI()

def my_custom_sum(a, b):
    return a + b


@app.get("/")
async def root(name: str=None):
    if name is None:
        return {"message": "Hello World"}
    else:
        return {"message": "Hello {name}! How are you?".format(name=name)}

@app.get("/sum")
async def sum(a: int=0, b: int=0):
    return {"result": my_custom_sum(a, b)}