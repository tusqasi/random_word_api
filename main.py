from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

words = []
with open("words.txt",mode='r') as fp:
    words  = fp.readlines()[0].split(" ")

@app.get("/")
async def root():
    return "Default route laksdjfoijisdj10dns"

@app.get("/word")
async def one_word():
    return {"word" : random.choice(words)}

@app.get("/words/{n}")
async def multiple_words(n:int):
    return {"words" : random.choices(words, k=9)}
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info",reload=True)


