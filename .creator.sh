#!/bin/bash

function create() {
    source .env
    python3 create.py $1
    cd $WORKSPACEPATH
    flutter create --org com.moonviral $1
    cd $1
    git init
    git remote add origin https://$USERNAME@github.com/$USERNAME/$1.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}
