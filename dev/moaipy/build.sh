#!/bin/bash

# build python extension
rm -f moaipy.cpp

# PYTHON_PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin/python"
export MACOSX_DEPLOYMENT_TARGET=10.11
# $PYTHON_PATH setup.py build
python setup.py build

echo "=== LIBRARY BUILT ==="

cd 'build/'

dir1=$(find . -name lib.\* -type d -maxdepth 1 -print | head -n1)
cd "$dir1"

echo "overriding loader path for libfmod.dylib ..."
install_name_tool -change "@rpath/libfmod.dylib" "@loader_path/libfmod.dylib" moaipy.so
echo "moving moaipy.so to editor/moaipy/moaipy.so ..."
cp moaipy.so '../../../../editor/lib/moaipy/moaipy.so'
echo "=== COMPLETE ==="