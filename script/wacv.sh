
MAIN_DIR=${0%/*}/..
SRC=src/main.py

TITLE=wacv
YEAR=2023
TYPE=main

pushd $MAIN_DIR

python3 $SRC \
  --title=$TITLE \
  --year=$YEAR \
  --type=$TYPE

popd