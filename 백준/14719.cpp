#include <iostream>
#include <algorithm>
using namespace std;
int arr[501];
int H, W;

int main()
{
	cin >> H >> W;
	for (int i = 0; i < W; i++)
		cin >> arr[i];

	int answer = 0;

	for (int i = 1; i < W - 1; i++) {
		int left = arr[i], right = arr[i];

		for (int j = 0; j < i; j++) {
			left = max(left, arr[j]);
		}
		for (int j = i + 1; j < W; j++) {
			right = max(right, arr[j]);
		}
		int cur = min(left, right);
		answer += cur - arr[i];
	}

	cout << answer << endl;
}