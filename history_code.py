import pandas as pd 

filepath="D:\学习\CPK自动化工具\data\FQ29PB007A-20230131_105159_NSFT_PASS.csv"  #文件路径
file = pd.read_csv(filepath,header=0,index_col='TEST')   #hearder=0--选第一行作为列索引；index_col='TEST'--选“TEST”列作为行索引
#print(file)
file1=file[['L_LIMIT','U_LIMIT']]  #选择上限"L_LIMIT"和下限“U_LIMIT”两列
#print(file1)
file_title=file1.T  #转置,得到常规表头
#print(file_title)  
file_title.to_excel('D:\学习\CPK自动化工具\data\CPK_title.xlsx')  #表头写到EXCEL表


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

f_path=r'D:\Study\CPK_Automate_Tool\test\FQ29PB006M-20230131_023809_NSFT_PASS_1.txt'
with open(f_path,'r',encoding = 'utf-8') as f:
    temp = f.read() #导入文件
    #print(temp)
line_list = temp.splitlines() #将文件按行转化为列表
#print(line_list)
front=line_list.index('[TEST_DATA]') #检索开始标识[TEST_DATA]的索引值
end=line_list.index("[TEST_RESULT]")#检索结束标识[TEST_RESULT]的索引值
list_need=line_list[front+1:end] #截取开始标识及结束标识之间的数据
#print(list_need)
list_end=[]
for i in list_need:   #遍历列表中的元素字符串
    #print(i)
    #print(i.split('='))
    #print(i.split('=')[1])
    test_value=i.split('=')[1] #使用分隔符“=”拆分字符串并获取索引为1的等号右边的测试值
    list_end.append(test_value) #将测试值填入列表

#print(list_end)
"""
line_list = temp.splitlines() #将文件按行转化为列表
#print(line_list)
front=line_list.index('[TEST_DATA]') #检索开始标识[TEST_DATA]的索引值
end=line_list.index("[TEST_RESULT]")#检索结束标识[TEST_RESULT]的索引值
list_need=line_list[front+1:end] #截取开始标识及结束标识之间的数据
print(list_need)

list_end=[]
for i in list_need:   #遍历列表中的元素字符串
    #print(i)
    #print(i.split('='))
    #print(i.split('=')[1])
    test_value=i.split('=')[1] #使用分隔符“=”拆分字符串并获取索引为1的等号右边的测试值
    list_end.append(test_value) #将测试值填入列表

print(list_end)
"""