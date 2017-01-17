#!/usr/bin/bash



echo '''
Copyright (C) 2016 Sminq India Solutions Pvt Ltd.
Created on 2017-01-11
Updated on 2017-01-15

 ____    __  __   ___   _   _    ___
/ ___|  |  \/  | |_ _| | \ | |  / _ \
\___ \  | |\/| |  | |  |  \| | | | | |
___) |  | |  | |  | |  | |\  | | |_| |
|____/  |_|  |_| |___| |_| \_|  \__\_\


@author: Karuna Lingham
'''

echo "================================="
echo "Sminq User iOS App v1.2.3 ..."
echo "Running Test Suite v1.0.1 ..."
echo "================================="

d="$(date +'%d-%m-%Y')"
t="$(date +%H:%M)"
now=$d-$t

start=`date +%s`

#Run scripts
for folder in ./*
do

   #Begin recording tests for every folder
   echo "------------------"
   echo "$folder"
   echo "------------------"

  #Begin iterating through every file in specified folder
  for fname in $folder/*.py
  do

    #Execute file
    python $fname
    # total_count=$((total_count + 1))

  done
done

#Test count and timer
end=`date +%s`
total_time=$((end-start))

echo "================================="
echo "Time taken for sminq iOS test suite: $total_time sec."
echo "================================="
