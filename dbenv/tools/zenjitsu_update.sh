#!/bin/bash
dbenv='/mnt/horseracing/predict/dbenv/JRA'
git_lib='/mnt/horseracing/predict/git_lib/dbenv'
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
