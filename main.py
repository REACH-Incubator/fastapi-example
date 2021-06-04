from fastapi import FastAPI

app = FastAPI()

def my_custom_sum(a, b):
    return a + b - 1


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sum")
async def sum(a: int=0, b: int=0):
    return {"result": my_custom_sum(a, b)}