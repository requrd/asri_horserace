#!/bin/bash
dbenv='/mnt/horseracing/predict/dbenv/JRA'
git_lib='/mnt/horseracing/predict/git_lib/dbenv'
ymd=$1
echo 'バックアップ開始'
cp $dbenv/jrdb.db $dbenv/jrdb_${ymd}_seiseki_bk.db
echo 'バックアップ完了!'
mkdir 'work'
cd ./work
echo 'モジュール類のコピー開始'
echo 'DBファイルコピー開始'
cp $dbenv/jrdb.db ./
echo 'DBファイルコピー完了'
echo 'モジュールコピー開始'
cp $git_lib/database_setup.py ./
cp $git_lib/domain/add_sed.py ./
cp $git_lib/domain/add_srb.py ./
cp $git_lib/domain/add_hjc.py ./
cp $git_lib/tools/download_results.py ./
echo 'モジュールコピー完了'
echo '更新処理開始'
python download_results.py $ymd
python add_sed.py SED${ymd:2:8}.txt
python add_srb.py SRB${ymd:2:8}.txt
python add_hjc.py HJC${ymd:2:8}.txt
echo '更新完了'
mv jrdb.db $dbenv
cd ..
rm -R ./work
echo 'jrdb.db moved!'
