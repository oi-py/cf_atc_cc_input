_local_debug_ = True

##############题目###############
'''
https://codeforces.com/contest/{contest_id}/problem/{problem_id}
https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{problem_id}
'''
##############规律###############
#规律1：
#规律2：
#规律3：

##############猜想###############
#猜想1：
#证明1：
#猜想2：
#证明2：
#猜想3：
#证明3：

##############简化的问题###############
#问题1：
#问题2：
#问题3：

##############解法###############
# 解法1：
# 解法2：
# 解法3：

##############用例###############
#输入1：
#输出1：
#输入2：
#输出2：
#输入3：
#输出3：

##############实现###############

import time
import sys

input = sys.stdin.readline

is_debug = '_local_debug_' in globals()

#int input
def inp():
    return(int(input()))

#list input
def inlt():
    return(list(map(int,input().split())))

#string input
def insr():
    return input()[:-1]

#variables input
def invr():
    return(map(int,input().split()))

#matrix input
def inmt(n):
    return [inlt() for _ in range(n)]

##############实现层###############
class Solution(object):
    def input(self):
        # 读入数据，返回一个参数列表
        # 例如：读取一个整数n和一个字符串s
        # return (n, s)
        return None

    def solve(self, x):
        return x

    def output(self,ans):
        print(ans)

##############接口层###############
def solve():
    sol = Solution()
    x = sol.input()
    ans = sol.solve(x)
    sol.output(ans)

##############样例层###############
#样例数量，对于只有一个样例的题目，将inp()改为1
t = inp() 
#t = 1
for i in range(1, t + 1):
    if is_debug: start = time.time()
    solve()
    if is_debug:
        end = time.time()
        print('Case #{}: {} ms'.format(i, (end - start) * 1000))