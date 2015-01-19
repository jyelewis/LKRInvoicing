#!/bin/bash
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "deleting last build"
rm -rf /tmp/serverBuild

echo "copying directory"
cd ${DIR}

cp -r . /tmp/serverBuild

echo "removing unnecessary files"
rm /tmp/serverBuild/buildServer.sh
rm -rf /tmp/serverBuild/__pycashe__
rm /tmp/serverBuild/*.pyc
if [ -d "/tmp/serverBuild/serverSpecific" ]; then
	rm -r /tmp/serverBuild/serverSpecific
fi

rm -f /tmp/serverBuild/serverBuild.zip

if [ -d "./serverSpecific" ]; then
	echo "copying in build specific files"
	rsync -av ./serverSpecific/* /tmp/serverBuild
fi

echo "zipping build"
cd /tmp/serverBuild
zip -r /tmp/serverBuild.zip *


echo "moving zip to directory"
cd ${DIR}
mv /tmp/serverBuild.zip ./serverBuild.zip

echo "completed"