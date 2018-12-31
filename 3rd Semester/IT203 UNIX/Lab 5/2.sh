#!/bin/bash

echo "Enter choice based on operation:"
echo "1) Add record to database"
echo "2) Delete record from database"
echo "3) Find record in database"
echo "Enter choice based on operation:"
read choice

case $choice in
	1)
	echo "Enter roll no."
	read rollno

	if grep "$rollno" database.txt
	then
		echo "Roll number already in database!"
		exit 0
	fi

	echo "Enter name"
	read name
	echo "Enter semester"
	read sem
	echo "Enter marks scored in English"
	read eng_marks
	echo "Enter marks scored in Maths"
	read math_marks
	echo "Enter marks scored in Computers"
	read comp_marks

	echo "$rollno|$name|$sem|$eng_marks|$math_marks|$comp_marks" >> database.txt
	echo "New database:"
	cat database.txt
	;;
	2)
	echo "Enter roll no."
	read rollno

	if grep "$rollno" database.txt
	then
		:
	else
		echo "Roll number not in database!"
		exit 0
	fi

	sed -i "/$rollno/d" database.txt
	echo "New database:"

	cat database.txt

	;;
	3)
	echo "Enter roll no."
	read rollno

	grep "$rollno" database.txt

	;;
	*) 
	echo "Invalid choice entered"
	;;

esac