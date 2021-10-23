#include <stdio.h>
int main()
{
    int N, one, ten,NNN;
    int NN = 0;
    int count = 0;
    scanf("%d", &N);
    NN = N;
    while(1)
    {
        ten = NN / 10;
        one = NN % 10;
        NNN = ten + one;
        NNN = NNN % 10;
        NN = 10 * one + NNN;
        count = count + 1;
        if(NN == N)
            break;
    }
    
    printf("%d",count);
    return 0;
}
