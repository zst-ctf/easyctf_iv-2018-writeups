#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv){
    srand(time(0));
    int secret = rand();
    printf("name\n"); // Enter your name: 
    printf("%x\n", secret);
    return 0;
}

