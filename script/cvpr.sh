
MAIN_DIR=${0%/*}/..
SRC=src/main.py

TITLE=cvpr
YEAR=2022
TYPE=main

pushd $MAIN_DIRq

python3 $SRC \
  --title=$TITLE \
  --year=$YEAR \
  --type=$TYPE

popd