#include <stdio.h>
              
int main() {
int a = 2;
int b = 2;
int c = a + b;
// Define an array of strings
char* listOfUsers[] = {"User1", "User2", "User3"};
int numberOfUsers = sizeof(listOfUsers) / sizeof(listOfUsers[0]);

// Print the list of users
for (int i = 0; i < numberOfUsers; i++) {
    printf("%s\n", listOfUsers[i]);
}           
printf("C says: Hello, World!\n");
printf("%d + %d = %d\n",a,b,c);
              
return 0;
}

