#!/bin/bash

###環境変数設定###
###bashrcに記載の内容を転記###
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
export PATH="$PYENV_ROOT/versions/miniconda3-4.3.30/bin/:$PATH"
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
. /home/requrd/.pyenv/versions/miniconda3-4.3.30/etc/profile.d/conda.sh

###DB,モジュール保存場所###
dbenv='/mnt/horseracing/predict/dbenv/NAR'
git_lib='/mnt/horseracing/predict/git_lib/scraping/local'

###処理開始###
conda activate tensorflow #minicondaの環境で実行
ymd=$1
echo 'バックアップ開始'
cp $dbenv/kichiuma.db $dbenv/kichiuma_${ymd}_result_bk.db
echo 'バックアップ完了!'
cd /home/requrd
mkdir 'work'
cd ./work
echo 'モジュール類のコピー開始'
echo 'DBファイルコピー開始'
cp $dbenv/kichiuma.db ./
echo `ls`
echo 'DBファイルコピー完了'
echo 'モジュールコピー開始'
cp $git_lib/kichiuma_setup.py ./
cp $git_lib/courseutil.py ./
cp $git_lib/add_result_nar.py ./
echo `ls`
echo 'モジュールコピー完了'
echo '更新処理開始'
python add_result_nar.py $ymd
echo '更新完了'
mv kichiuma.db $dbenv
cd ..
rm -R ./work
echo 'jrdb.db moved!'
