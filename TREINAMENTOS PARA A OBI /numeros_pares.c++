#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int soma = 0;

    for (int x : nums) {
        soma += x;
    }

    cout << soma << '\n';
}