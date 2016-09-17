#! /bin/bash

SERVER="127.0.0.1"
USERNAME="deepesh"
DATABASE="database"
echo "Dumping of data of $DATABASE from $SERVER"

ssh $USERNAME@$SERVER mysqldump --complete-insert --lock-all-tables --no-create-db --no-create-info --extended-insert=FALSE --password=root -u root $DATABSE > $DATABASE.sql

scp $USERNAME@$SERVER:~/$DATABASE.sql $HOME/$DATABASE.sql
