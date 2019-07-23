# Analys tools for horseracing
jrdb絡みのものは移管済み。
メインで使うのは、トレーニングデータ向けのutilが中心。

全体的にAstrorippleへ移管予定。

# Dockerfile
`docker build ./ -t nvidia-conda`  
`docker run --name jupyter-lab -p 8888:8888 -it nvidia-conda`  