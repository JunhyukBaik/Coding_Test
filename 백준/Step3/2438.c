#include <stdio.h>

int main()
{
    int i;
    scanf("%d", &i);
    
    for (int j = 1; j <= i; j++)
    {
        for(int k = i - j; k < i; k++)
            printf("*");
        printf("\n");
    }
    return 0;
}