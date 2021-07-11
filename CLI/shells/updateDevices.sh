#!/bin/bash
source $HOME/habcatpi/CLI/shells/constants.sh 

echo "****** Updating Devices ******"
set -x
rm -rf $DEVICES_PATH
mkdir $DEVICES_PATH

cd /tmp
rm -rf $COMPONENTS_REPO_NAME
git clone "$COMPONENTS_REPO"
cp -R $COMPONENTS_REPO_NAME"/Devices/." $DEVICES_PATH
rm -rf /tmp/$COMPONENTS_REPO_NAME
set +x

ls $DEVICES_PATH