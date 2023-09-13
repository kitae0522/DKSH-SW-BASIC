#!/bin/sh

cp .setup_git/.gitmessage .git/.gitmessage
cp .setup_git/hooks/* .git/hooks

git config --local commit.template .git/.gitmessage
