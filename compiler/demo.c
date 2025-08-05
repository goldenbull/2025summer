/*
    this is a block comment
*/

#define MAX 1000
#define ADD(x,y) (x+y)

#include <stdio.h>

int f3();
int f2(void);
extern int global_x;
int global_y;
int global_z = 1.23;
double f1 = 12.3;
int f1(int x){if(x<10)return 100;else return 300;}

void main()
{
    #define MAX 1000
    int a = ADD(1,2);
    int b = (1+2);

    int arr[10];
    int arr2[20] = {1,2,3};

   if(a>b)
   {
    a=2;
   }
   else
   {
   }

   for(int a=1;a>b;a=a+1)
   {
   }

   for(a=1;a>b;a=a+1)
   {
   }

}