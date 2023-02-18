_local_debug_ = True

'''
https://codeforces.com/contest/{contest_id}/problem/{problem_id}
https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{problem_id}
题目：

'''
'''
将以上题目翻译成中文：

'''
'''
将以上题目中的故事描述转化为易于编程的技术性语言：

'''

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

    def solve(self, param):
        return param

    def output(self,ans):
        print(ans)

##############接口层###############
def solve():
    sol = Solution()
    param = sol.input()
    ans = sol.solve(param)
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
