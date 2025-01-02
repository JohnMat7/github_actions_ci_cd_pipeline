from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Hi John Welcome Man!  (messaged added)"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7000, reload=True)