from fastapi import FastAPI
from pydantic import BaseModel
from main import prompt

app=FastAPI()

class compare_request(BaseModel):
    resume:str
    jd:str
    
@app.post("/compare")
async def comparision(req:compare_request):
    
    try:
        response=prompt(req.resume,req.jd)
        print(response)
        return {"status":"success","result":response}
    except Exception as e:
        return {"status":"error","message":str(e)}
    
    
        