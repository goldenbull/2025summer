/* 块注释测试 */
// 行注释测试
#define TEST 1

extern int extern_declared_var;
extern float extern_defined_var;

int declared_var;
float defined_var = 2.718;
char char_array[10];
long initialized_array[3] = {1L, 2L, 3L};

void void_function();
int add(int a, int b);
int compare(int a, int b);

int add(int a, int b)
{
    return a + b;
}

int compare(int a, int b)
{    
    if (a > b) // this is comment
        return 1;
    if (a < /* embedded */ b)
        return -1;
    return 0;
}

void void_function()
{

    short short_var;
    double double_var = 3.1415926;

    declared_var = 42;
    char_array[0] = 'A';

    if (declared_var > 0)
        if (defined_var < 10)
        {
            int result = TEST - 2;
        }
        else
        {
            int result = 0;
        }

    int i = 0;
    while (i < 5)
    {
        i = i + 1;
    }

    for (int j = 0; j < 5; j = j + 1)
    {
        if (j == 2)
        {
            continue;
        }
        if (j == 4)
        {
            break;
        }
    }

    int sum = add(10, 20);

    int arr[3] = {1, 2, 3};
    int val = arr[1];
    arr[2] = 5;

    return;
}

int main()
{
    int x=-5;
    int y=10;

    int z = ((x-5)*2+y)/3%-10;

    int cmp = compare(x, y);
    int mod = z % 3;
    int logical = (x > 0) && (y < 20) || (z == 30);

    int sum = add(x, y);

    return sum;

    int a = 2-1;
}