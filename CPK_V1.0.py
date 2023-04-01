df = pd.read_csv(r"E:\Python学习\test.txt")
print(df)


import os
import pandas
import codecs
import glob
import pandas as pd
os.getcwd() #返回当前工作目录
os.chdir('D:\学习\CPK自动化工具\data\demo')  #改变当前工作目录到指定的路径。
#def txtcombine():
files = glob.glob('*.txt')
all = codecs.open('all.txt','a')
for filename in files:
    print(filename)
'''
        fopen=codecs.open(filename,'r',encoding='utf-8')
        lines=[]
        lines=fopen.readlines()
        fopen.close()
        i=0
        for line in lines:
            for x in line:
                all.write(x)
        #读取为DataFrame格式
        all1 = pd.read_csv('all.txt',sep=' ',encoding='GB2312')
        #保存为csv格式
        all1.to_csv('all.csv',encoding='GB2312')
if __name__ == '__main__':
    txtcombine()


'''

