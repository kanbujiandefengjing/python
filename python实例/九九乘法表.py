#coding:utf-8
#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('{}×{}={}\t'.format(i,j,i*j),end='')
    print()
