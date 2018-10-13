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
dbenv='/mnt/horseracing/predict/dbenv/JRA'
git_lib='/mnt/horseracing/predict/git_lib/dbenv'

###処理開始###
conda activate tensorflow #minicondaの環境で実行
ymd=$1
echo 'バックアップ開始'
cp $dbenv/jrdb.db $dbenv/jrdb_${ymd}_bk.db
echo 'バックアップ完了!'
mkdir 'work'
cd ./work
echo 'モジュール類のコピー開始'
echo 'DBファイルコピー開始'
cp $dbenv/jrdb.db ./
echo 'DBファイルコピー完了'
echo 'モジュールコピー開始'
cp $git_lib/database_setup.py ./
cp $git_lib/domain/add_bac.py ./
cp $git_lib/domain/add_cha.py ./
cp $git_lib/domain/add_cyb.py ./
cp $git_lib/domain/add_kab.py ./
cp $git_lib/domain/add_kyi.py ./
cp $git_lib/master/add_ukc.py ./
cp $git_lib/tools/download_paci.py ./
echo 'モジュールコピー完了'
echo '更新処理開始'
python download_paci.py $ymd
python add_bac.py BAC${ymd:2:8}.txt
python add_cha.py CHA${ymd:2:8}.txt
python add_cyb.py CYB${ymd:2:8}.txt
python add_kab.py KAB${ymd:2:8}.txt
python add_kyi.py KYI${ymd:2:8}.txt
python add_ukc.py UKC${ymd:2:8}.txt
echo '更新完了'
mv jrdb.db $dbenv
cd ..
rm -R ./work
echo 'jrdb.db moved!'
