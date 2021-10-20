#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++)
    {
        for (int j = i + 1; j <= N; j++)
            printf(" ");
        for (int k = N - i; k < N; k++)
            printf("*");
        printf("\n");
    }
    return 0;
}