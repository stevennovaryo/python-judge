// solution for https://tlx.toki.id/problems/troc-12/B
#include <bits/stdc++.h>
using namespace std;

int N;
long long A[31], sum;

int main() {
    scanf("%d", &N);
    for(int i = 0; i <= N; i++) {
        scanf("%lld", &A[i]);
        sum += A[i] << i;
    }
    if(sum % (1LL << N)) puts("-1");
    else printf("%lld\n", sum / (1LL << N));
    return 0;
}
