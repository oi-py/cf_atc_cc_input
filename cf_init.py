'''
复制该文件夹下的A.py到以下文件（如果文件存在，直接替换；如果不存在，创建该文件）：
A2.py
B.py
B2.py
C.py
C2.py
D.py
D2.py
E.py
E2.py
F.py
F2.py
G.py
G2.py
H.py
H2.py
I.py
I2.py

对于A.rs文件，执行同样的操作，覆盖A2.rs,B.rs……I2.rs
对于A.cpp文件，执行同样的操作，覆盖A2.cpp,B.cpp……I2.cpp
对于A.c文件，执行同样的操作，覆盖A2.c,B.c……I2.c
'''
import os
import shutil
import sys

def copy_file(src, dst):
    if os.path.exists(dst):
        os.remove(dst)
    shutil.copy(src, dst)

def replace_str_in_file(file_path, old_str, new_str):
    new_str = new_str.lower()
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(file_path, 'w', encoding='utf-8') as f_w:
        for line in lines:
            f_w.write(line.replace(old_str, new_str))

def copy_files(contest_id,suf):
    src = '0.' + suf
    for i in range(9):
        ch = chr(ord('A') + i)
        dst = ch + '.' + suf
        if src != dst:
            copy_file(src, dst)
            #将dst文件中的{contest_id}替换为contest_id，将{problem_id}替换为ch
            replace_str_in_file(dst, '{contest_id}', contest_id)
            replace_str_in_file(dst, '{problem_id}', ch)
            print('copy {} to {}'.format(src, dst))
        dst = ch + '2.' + suf
        copy_file(src, dst)
        #将dst文件中的{contest_id}替换为contest_id，将{problem_id}替换为ch2
        replace_str_in_file(dst, '{contest_id}', contest_id)
        replace_str_in_file(dst, '{problem_id}', ch+'2')
        print('copy {} to {}'.format(src, dst))

def main():
    #读取第一个参数，作为比赛id
    if len(sys.argv) < 2:
        print('please input contest id')
        contest_id = input()
    else:
        contest_id = sys.argv[1]
    copy_files(contest_id,'py')
    copy_files(contest_id,'cpp')
    copy_files(contest_id,'c')
    print('Done')

if __name__ == '__main__':
    main()