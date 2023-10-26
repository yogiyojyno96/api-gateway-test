from fastapi import FastAPI

app2 = FastAPI()

@app2.get("/")
def read_root():
    return {"Hello": "from Service b"}