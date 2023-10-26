from fastapi import FastAPI

app1 = FastAPI()

@app1.get("/")
def read_root():
    return {"Hello": "from Service a"}