# Analysis tools for horseracing
jrdb絡みのものは移管済み。
メインで使うのは、トレーニングデータ向けのutilが中心。

全体的にAstrorippleへ移管予定。

## Development
```
docker build ./ -t nvidia-conda  
docker run --gpus=all --rm -v `pwd`:/code -p 8888:8888 --name jupyter -it nvidia-conda  
```
## DBの更新
Batchコンテナを利用して、MariaDBを更新する。  
https://github.com/astroripple/batch