from typing import Optional
from fastapi import Depends, FastAPI
import uvicorn
import logging
import pandas as pd
import numpy as np
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sake_bert import SakeBert 

app = FastAPI()
logger = logging.getLogger('uvicorn')
logger.setLevel(logging.DEBUG)
#mecab = MeCab.Tagger('-Owakati')
## ストップワード(pos指定)
#stopWords = ["BOS/EOS", "助詞", "助動詞", "記号"]

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
    result = np.round(sake.marige(q) * 100, 3)
    logger.info(type(result))
    logger.info(result)
    best = np.argmax(result)
    
    sakeType = SakeBert.SakeType[best]
    return {"status": "OK", "result": f"{result} 最も合う日本酒のタイプ={best} {sakeType}"}
