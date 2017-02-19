#!/bin/bash

for i in *.cc
do
    if ! grep -q COPYRIGHT.txt $i
	then
	cat cp.txt $i >$i.new && mv $i.new $i
	fi
done

for i in *.cpp
do
    if ! grep -q COPYRIGHT.txt $i
	then
	cat cp.txt $i >$i.new && mv $i.new $i
	fi
done

for i in *.h
do
    if ! grep -q COPYRIGHT.txt $i
	then
	cat cp.txt $i >$i.new && mv $i.new $i
	fi
done
#sf
