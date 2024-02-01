#!/bin/bash
              
a=2
b=2
c=$((a + b))
              
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

# Define an array of strings
listOfUsers=("User1" "User2" "User3")

# Print the list of users
for user in "${listOfUsers[@]}"; do
    echo "$user"
done

