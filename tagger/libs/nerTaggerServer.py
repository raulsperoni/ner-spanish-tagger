#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,jsonify,request
import time,os,threading,sys,traceback
import requests
import es_core_news_md
import logging
from pprint import pprint, pformat



def doTheHardWork(data,id):
    with app.app_context():
        try:
            coordinates = data.get('coordinates',None)
            callback = data.get('callback',None)
            text = data.get('text',None)
            error = False
            logger.info('Working: ')
            if callback and text:
                start = time.time()
                solutions = nlp(data['text'])
                end = time.time()
                requests.post(callback, json={"id":id,"solutions":solutions,"time":str(end-start),"error":False})
                logger.info('Done.'+str(len(solutions))+'geoTags. Demora:'+str(end-start))
        except Exception as e:
            logger.error(e)
            traceback.print_exc(file=sys.stdout)


app = Flask(__name__)

@app.route('/api/print', methods=['POST'])
def log():
    data = request.get_json(silent=True)
    logger.info('CALLBACK '+pformat(data))
    return jsonify({}),200

@app.route('/api/find/<id>', methods=['POST'])
def find(id):
    data = request.get_json(silent=True)
    thread = threading.Thread(target=doTheHardWork, args = (data,id))
    thread.daemon = True
    thread.start()
    return 'OK'

if __name__ == '__main__':
    nlp = es_core_news_sm.load()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    app.run(debug=True,host='0.0.0.0')