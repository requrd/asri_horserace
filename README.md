# Analysis tools for horseracing
jrdb絡みのものは移管済み。
メインで使うのは、トレーニングデータ向けのutilが中心。

全体的にAstrorippleへ移管予定。

# Dockerfile
`docker build ./ -t nvidia-conda`  
``docker run --gpus=all --rm -v `pwd`:/code -p 8888:8888 --name jupyter -it nvidia-conda``  

# DBの更新
APIのコンテナを利用して、jrdb.dbの存在するディレクトリで更新する。  

前日更新  
``docker run --rm -v `pwd`:/code/volume -it sazanami-api /bin/bash /code/tools/database/zenjitsu_update.sh 20190211``  
成績系データ更新  
``docker run --rm -v `pwd`:/code/volume -it sazanami-api /bin/bash /code/tools/database/seiseki_update.sh 20190211``  

一括更新  
以下の日付を修正して実行する  
`./database_update.sh`
