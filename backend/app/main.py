from typing import Optional
from fastapi import FastAPI
import logging
import numpy as np
from sake_bert import SakeBert 

app = FastAPI()
logger = logging.getLogger('uvicorn')
logger.setLevel(logging.DEBUG)

sake = SakeBert()

@app.get("/api")
def root():
    logger.info("Root API called")
    return {"API Status": "OK"}

@app.get("/api/load")
def load():
    logger.info("Start load Bert")
    sake.load(logger)
    logger.info("End load Bert")
    return {"status": "OK"}

@app.get("/api/mariage")
def marige(q: Optional[str] = None, limit: Optional[int] = 3):
    logger.info(q)
    np.set_printoptions(formatter={'float' : "{:.3f}".format })
    result = sake.marige(q) * 100
    logger.info(result)
    best = np.argmax(result)
    
    sakeType = SakeBert.SakeType[best]
    return {"status": "OK", "result": f"{result}\n最も合う日本酒のタイプ={best}\n{sakeType}"}
