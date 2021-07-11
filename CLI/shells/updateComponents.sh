#!/bin/bash
source $HOME/habcatpi/CLI/shells/constants.sh 

echo "****** Updating Componets ******"
set -x
rm -rf $COMPONENTS_PATH
mkdir $COMPONENTS_PATH

cd /tmp
rm -rf $COMPONENTS_REPO_NAME
git clone "$COMPONENTS_REPO"
cp -R $COMPONENTS_REPO_NAME"/Components/." $COMPONENTS_PATH
rm -rf /tmp/$COMPONENTS_REPO_NAME
set +x

ls $COMPONENTS_PATH