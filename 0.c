#define _local_debug_

// 将以上Python代码转化为c代码

#include <stdio.h>
#include <time.h>

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

void read_list(int *list, int n){
    for(int i = 0; i < n; i++){
        scanf("%d", &list[i]);
    }
}

void read_matrix(int *matrix, int n, int m){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &matrix[i * m + j]);
        }
    }
}

void solve(){
    printf("Yes\n");
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        #ifdef _local_debug_
            clock_t start = clock();
        #endif
        solve();
        #ifdef _local_debug_
            clock_t end = clock();
            printf("Case #%d: %lf ms\n", i, (double)(end - start) / CLOCKS_PER_SEC * 1000);
        #endif
    }
    return 0;
}