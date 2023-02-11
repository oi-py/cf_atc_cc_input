#define _local_debug_

// 将以上Python代码转化为cpp代码

#include <bits/stdc++.h>
using namespace std;

#define LL long long

void read_int(int *x){
    scanf("%d", x);
}

void read_int2(int *x, int *y){
    scanf("%d %d", x, y);
}

void read_int3(int *x, int *y, int *z){
    scanf("%d %d %d", x, y, z);
}

void read_int4(int *x, int *y, int *z, int *w){
    scanf("%d %d %d %d", x, y, z, w);
}

void read_str(char *s){
    scanf("%s", s);
}

void read_list(vector<int> &v, int n){
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        v.push_back(x);
    }
}

void read_matrix(vector<vector<int>> &v, int n, int m){
    for(int i=0; i<n; i++){
        vector<int> row;
        for(int j=0; j<m; j++){
            int x;
            cin>>x;
            row.push_back(x);
        }
        v.push_back(row);
    }
}

void solve(){
    cout<<"Yes"<<endl;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        #ifdef _local_debug_
            clock_t start = clock();
        #endif
        solve();
        #ifdef _local_debug_
            clock_t end = clock();
            cout << "Case #" << i << ": " << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << endl;
        #endif
    }
    return 0;
}