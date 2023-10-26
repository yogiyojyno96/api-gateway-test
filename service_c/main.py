from fastapi import FastAPI

app3 = FastAPI()

@app3.get("/")
def read_root():
    return {"Hello": "from Service c"}