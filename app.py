import uvicorn
from fastapi import FastAPI
import os
import api

app = FastAPI()
app.include_router(api.api)

@app.get("/")
def home():
    return {"message": "Hello!"}
 
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=3030, debug=True)
