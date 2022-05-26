import numpy as np
import tensorflow as tf
import transformers
from transformers import AutoModel, AutoTokenizer
from keras.preprocessing.text import Tokenizer
import os
import logging

class SakeBert:    
    max_length = 50
    SakeType = {0:"醇酒", 1:"薫酒", 2:"爽酒", 3:"熟酒"}
    model = None
    tokenizer = None

    def __init__(self):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        model_name = "cl-tohoku/bert-base-japanese-v2"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    # テキストのリストをtransformers用の入力データに変換
    def to_features(self, texts, max_length):
        shape = (len(texts), max_length)
        # input_idsやattention_mask, token_type_idsの説明はglossaryに記載(cf. https://huggingface.co/transformers/glossary.html)
        input_ids = np.zeros(shape, dtype="int32")
        attention_mask = np.zeros(shape, dtype="int32")
        token_type_ids = np.zeros(shape, dtype="int32")
        for i, text in enumerate(texts):
            encoded_dict = self.tokenizer.encode_plus(text, max_length=max_length, padding='max_length')
            input_ids[i] = encoded_dict["input_ids"]
            attention_mask[i] = encoded_dict["attention_mask"]
            token_type_ids[i] = encoded_dict["token_type_ids"]
        return [input_ids, attention_mask, token_type_ids]
    
    def load(self, logger):
        if(self.model == None):
            logger.info("Start load SakeBert")
            try:
                custom_objects = {"TFBertModel": transformers.TFBertModel}
                with tf.keras.utils.custom_object_scope(custom_objects):
                    logger.info('loading SakeBert')
                    self.model = tf.keras.models.load_model("../data/model")
            except:
                logger.error('Error load SakeBert')

    def marige(self, testdata):
        x_test = self.to_features([testdata], self.max_length)
        y_pred = self.model.predict(x_test).reshape([4])
        return y_pred
