#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d", &a);
    scanf("%d", &b);
    int c = b / 10;
    printf("%d\n", a*(b%10));
    printf("%d\n", a*(c%10));
    printf("%d\n", a*(c/10));
    printf("%d\n", a*b);
    
    return 0;
}