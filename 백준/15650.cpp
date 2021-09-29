#include <iostream>
#include <vector>
using namespace std;
#define MAX 9

int N, M;
int outp[MAX];
bool visited[MAX];

void nmn(int depth, int cnt)
{
    if (cnt == M) {
        for (int i = 0; i < M; i++) {
            cout << outp[i] << ' ';
        }
        cout << "\n";
        return;
    }

    for (int i = depth; i <= N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            outp[cnt] = i;
            nmn(i + 1, cnt + 1);
            visited[i] = false;
        }
    }
}

int main()
{
    cin >> N >> M;

    nmn(1, 0);

    return 0;
}