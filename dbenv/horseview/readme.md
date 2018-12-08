**使い方**
horseview フォルダをjrdb.dbと同じディレクトリに格納する。
horseview.horsemodelから用途に応じたクラスをインポートする。

*ロード例
from  horseview.horsemodel import KaisaiData
kaisais = KaisaiData.query.filter_by(ymd='20181118').all()
