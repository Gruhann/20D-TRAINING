#include<stdio.h>
int main()
{
    int a=12;
    if(a%1)//compares binary of 12 and 1 with and , 
    {         // if result is 0000 implies even else 0001 implies odd
        printf("odd");//1 implies if block and 0 implies else block
    }
    else
    {
        printf("even");
    }
}