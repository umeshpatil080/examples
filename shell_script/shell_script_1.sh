#! /usr/bin/bash

# # Print text to console
# echo Hello World

# # Reading input from the console
# echo -n "Enter your name:"
# read NAME
# echo "Entered name is '$NAME'"


# # Variable name: Convention is to use capital letters.
# # Can contain alph-numeric and underscore('_'). Start with aplhabet or '_'.
# # No space around '='
# NAME="Sam"
# echo "Name is $NAME"

# # Readonly variable
# NAME="Sam"
# readonly NAME
# # Below results in error
# NAME="Sam1"

# # Unsetting a variable
# # Cannot unset variables that are marked as readonly
# NAME="Sam"
# echo "Name is $NAME"
# unset NAME
# echo "Name after unsetting is $NAME"

# # Variable types
# # Type 1: Shell variable => Available to the instance of spawned shell. 
# # Try on command line
# # $ NAME="Sam"
# # $ source sam_shell_script.sh
# # Note: Sourcing executes script in same shell. It does not spawn new shell based on shebang line to execute the script.
# echo "Name is $NAME"

# # Type2: Envionment variables
# # $ export NAME="Sam"
# # $ ./sam_shell_script.sh
# echo "Name is $NAME"

# # Varible expansion
# NAME="Sam"
# echo "Name${NAME} is appears immdiately after 'Name' word"


# # Conditional operators
# NAME="Sam1"
# if [ "$NAME" == "Sam" ]
# then
#     echo "Name is $NAME"
# elif [ "$NAME" == "Abc" ]
# then
#     echo "Name is Abc"
# else
#     echo "Name is neither Sam nor Abc"
# fi


# # String comparision
# # string1 = string2 and string1 == string2 - The equality operator returns true if the operands are equal.
# # Use the = operator with the test [ command.
# # Use the == operator with the [[ command for pattern matching.
# VAR1="Windows"
# VAR2="RHEL is a Linux kernel based OS"
# if [ "$VAR1" != "$VAR2" ]
# then
#     echo "'$VAR1' and '$VAR2' are not same"
# fi

# # '[[]]' operator => No need to use double quote around variable name.
# # Can use regx
# VAR1="Windows"
# VAR2="RHEL is a Linux kernel based OS"
# if [[ $VAR1 != $VAR2 ]]
# then
#     echo "'$VAR1' and '$VAR2' are not same"
# else
#     echo "'$VAR1' and '$VAR2' are same"
# fi

# # Regex with '[[]]'
# VAR1="Linux"
# VAR2="RHEL is a Linux kernel based OS"
# if [[ $VAR2 =~ $VAR1 ]]
# then
#     echo "'$VAR2' contains '$VAR1'"
# else
#     echo "'$VAR2' does not contains '$VAR1'"
# fi

# # String emptiness
# VAR1=''
# if [ -z "$VAR1" ]
# then
#     echo "VAR1 is empty"
# else
#     echo "VAR1 is not empty"
# fi

# # String not empty check
# VAR2="sam data"
# if [ -n "$VAR2" ]
# then
#     echo "VAR2 is not empty"
# else
#     echo "VAR2 is empty"
# fi

# # Iterating over individual characters in a string
# VAR="shell_script"
# echo "Length: ${#VAR}"
# for (( i=0; i < ${#VAR}; i++))
# do
#     echo "Char at position $i: ${VAR:i:1}"
# done


# # case statement
# CITY="Bangalore"
# case $CITY in
#     "Bangalore")
#         echo -n "Match found"
#     ;;
#     "Bangalore" | "Mumbai")
#         echo -n "Match found in 'Bangalore|Mumbai'"
#     ;;
#     *)
#         echo -n "Match not found"
#     ;;
# esac


# # String cocatenation
# # Method1: Writing variables one after another
# VAR1="Hello,"
# VAR2=" World"
# VAR3="$VAR1$VAR2"
# echo "Concatenated string '$VAR3'"

# # Method2: Using += operator
# VAR1="Hello,"
# VAR1+=" World"
# echo "Concatenated string '$VAR1'"


# # Command line args
# echo "Script name: $0"
# echo "First arg: $1"
# echo "Total number of args: $#"
# # Splits cmd args by spaces even if enclosed within quotes
# # $* - is a single string
# # $ ./sam_shell_script.sh 1 2 '3 4'
# echo "Using \$*"
# for i in $*
# do
#     echo $i
# done

# # Honors quotes, does not split args based on space
# # $@ - is an actual array
# # $ ./sam_shell_script.sh 1 2 '3 4'
# echo "Using \$@"
# for i in "$@"
# do
#     echo $i
# done


# Arrays
# ARRAY=( "one" "two" "three" "four" "five" )
# for i in ${ARRAY[@]}
# do
#     echo $i
# done

# ARRAY=( "one" "two" "three" "four" "five" )
# echo "Length of array: ${#ARRAY[@]}"
# for (( i=0; i < ${#ARRAY[@]}; i++))
# do
#     echo ${ARRAY[i]}
# done