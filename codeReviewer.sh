#!/bin/bash
echo "Starting Code Review"
command -v meld >/dev/null 2>&1 || { echo >&2 "Please Install meld tool. Aborting Code Review."; exit 1; }
git ls-files --modified --others --exclude-standard | grep -v "target" | while read -r line ; do
        echo $line
	read -p "Do you want to continue? (y/n): " input < /dev/tty
    if [ $# -gt 0 ] ; then
        if [ $1 = "-an" -a $input = "y" ] ; then
            `git add $line`
        elif [ $1 = "-a" -a $input = "y" ] ; then
            `git add $line`
            meld $line
        fi
	elif [ $input = "y" ] ; then
        meld $line
	fi
done
