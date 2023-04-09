#导入数据分析pandas库
import pandas as pd #
#导入查找文件目录和文件名的模块
import glob 
#导入系统os库
import os

'''
#方法一：获取指定目录下符合条件文件的路径
#TXT文件路径字符串-*通配符：所有TXT文件
path = r"D:\Study\CPK_Automate_Tool\test\*.txt"
#将符合路径条件的TXT文件路径生成列表文件
all_file_path=glob.glob(path)
#print(all_file_path)
'''

#方法二：获取各子目录下文件路径
path=r'D:\Study\CPK_Automate_Tool\test'  #存放数据的根目录
# 获取所有文件的完整路径名
all_files_path=[]
for root,dirs,files in os.walk(path,topdown=False):   #os.walk()方法，是用于遍历文件目录，并返回目录名称的方法；root 所指的是当前正在遍历的这个文件夹的本身的地址；files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    
    #print(root)
    #print(dirs)
    #print(files)
    if len(files)>0:  #空文件夹没有文件的无需读取
        each_foder_files=[os.path.join(root,x) for x in files] #通过目录root+文件名file,合成每个文件的路径名
        #print(each_foder_files)
        all_files_path.extend(each_foder_files)

#print(all_files_path)







#创建空dataframe
#df_temp= pd.DataFrame(columns=['序号'])
#创建一个计数变量以读取的文件数量
#path_num=1

#读取第一个文件
df_temp=pd.read_csv(all_files_path[0],sep="=",header=3,usecols=[1],dtype={0:int})  #,nrows=40

#循环读取TXT文件到dataframe数据结构中
for path_each in all_files_path:
    #每个文件读取为1个dataframe
    df_each=pd.read_csv(path_each,sep="=",header=3,usecols=[1],dtype={0:int}) #,nrows=40
    #print(df_each)
    #不断合并dataframe
    df_temp=pd.concat([df_temp,df_each],axis=1,join='outer',ignore_index=True)
    #print(df_temp)

#print(df_temp)

#print(df_temp[0].dtypes)


'''
#文件保存路径
save_path=r'D:\Study\CPK_Automate_Tool\Result.csv'
#执行文件报告，不需要行索引和列索引
df_temp.to_csv(save_path,header=0,index=0)

'''


'''
f_path1= r"D:\Study\CPK_Automate_Tool\test\FQ29PB006M-20230131_023809_NSFT_PASS_1.txt"
f_path2= r"D:\Study\CPK_Automate_Tool\test\FQ29PB006Y-20230131_121817_NSFT_PASS.txt"
f_path3= r"D:\Study\CPK_Automate_Tool\test\FQ29PB006W-20230131_061339_NSFT_PASS.txt"

df1=pd.read_csv(f_path1,sep="=",header=3,usecols=[1],dtype={0:int},nrows=40) 
df2=pd.read_csv(f_path2,sep="=",header=3,usecols=[1],dtype={0:int},nrows=40) 
df3=pd.read_csv(f_path3,sep="=",header=3,usecols=[1],dtype={0:int},nrows=40) 

#print(df)

df0=pd.concat([df1,df2,df3],axis=1)  #按列进行拼接
print(df0)
'''

'''
    if len(files)>0:
        each_foder_files=[os.path.join(root,x) for x in files]
        #print(each_foder_files)
        all_files_path.extend(each_foder_files)
        #print(all_files_path)
'''