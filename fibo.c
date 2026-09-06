#include <stdio.h>

int fib(int n, int mem[])
{
    if (n <= 1)
        return n;

    if (mem[n] != -1)
        return mem[n];

    mem[n] = fib(n - 1, mem) + fib(n - 2, mem);

    return mem[n];
}

int main()
{
    int n = 10;
    int mem[10];

    for (int i = 0; i < n; i++)
        mem[i] = -1;

    for (int i = 0; i < n; i++)
        printf("%d ", fib(i, mem));

    return 0;
}
