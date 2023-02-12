_local_debug_ = True

'''
https://codeforces.com/contest/{contest_id}/problem/{problem_id}
https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{problem_id}
题目

'''
'''
解题过程
第一步:观察规律
通过观察显而易见的规律来寻找解题的方向(可以是题目中给出的信息的简单推导得出的结论，也可以是对解决此题有帮助的数学规律)

规律一:
规律二:
规律三:
第二步：证明该问题无法暴力解决
计算暴力解的时间复杂度
暴力解是否有可能通过此题?
暴力解是否存在优化的可能性？
第三步：猜规律
如果通过第一二步已经能够找到明确的解法，则跳过此步。

猜想一：
尝试证明：
尝试构造反例：
猜想二：
第四步：寻找可能的解题思路
思路一：
证明该方法可行
时间复杂度
是否可能通过
是否有模板?
实现需要的代码量
实现需要的时间
难度分评估
止损时间(15分钟?)
思路二：
第五步：简化问题
如果第四步已经找到解题思路，则跳过此步。 否则寻找简化版本的问题(难度分下降400以上)，先解决简化版本的问题，再解决此问题。

简化问题一:
问题描述
第六步：将样例复制到此处
样例一：
输入：
输出：
第七步：编写代码
在编写代码前，不可跳过前面六步，请按正确的过程解决问题。

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
