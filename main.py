from fastapi import FastAPI
 
app = FastAPI()

@app.get('/')
async def get_deneme():
    return {"message":" deneme 2"}