## フォルダ構成
##  app.pyを下記のフォルダに配置
##  horseview（jrdb.db接続用パッケージ）
##  jrdb.db
##  app.py

## how to use
##  下記コマンドを実行 
##  python -m flask run

from flask_cors import CORS
from horseview.horsemodel import KaisaiData,BangumiData,PredictData
from horseview.sessioncontroll import app,manager

CORS(app)

manager.create_api(KaisaiData,methods=["GET"],include_columns=['course_name','races'],collection_name='races')
manager.create_api(BangumiData,methods=["GET"],include_columns=['racehorses'],collection_name='racehorses')
manager.create_api(PredictData,methods=["GET"])
