#导入数据分析pandas库
import pandas as pd #
#导入查找文件目录和文件名的模块
import glob 
#导入系统os库
import os
#导入处理excel 文件的openpyxl库
import openpyxl


#选择/输出MES LOG 文件存放的根目录
path=r'D:\Study\CPK_Automate_Tool\test\sub1\sub11'  #存放数据的根目录

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


#读取第一个文件
#df_temp=pd.read_csv(all_files_path[0],sep="=",header=3,usecols=[1],dtype={0:int})  #,nrows=40

df_temp=pd.read_csv(all_files_path[0],sep="=")  #,nrows=40

#读取一个MES LOG TXT文件到dataframe
#df_temp=pd.read_csv(path,sep="=") 
#print(df_temp)

#获取dataframe中标志为[TEST_DATA]及[TEST_RESULT]的行号，因为所需数据在两个标志之间
row_start=df_temp.index.get_loc('[TEST_DATA]')
row_end=df_temp.index.get_loc('[TEST_RESULT]')
print(row_start)
print(row_end)

#截取[TEST_DATA]及[TEST_RESULT]两个标志之间的数据到dataframe
df_temp=pd.read_csv(all_files_path[0],sep="=",skiprows=lambda x:x<=row_start or x>=row_end+1,header=0,usecols=[1],dtype={0:int})  #,nrows=40  ,header=3,usecols=[1],dtype={0:int} skip_blank_lines=True
#print(df_temp)


#循环读取TXT文件到dataframe数据结构中
for path_each in all_files_path:
    #每个文件读取为1个dataframe
    #df_each=pd.read_csv(path_each,sep="=",header=3,usecols=[1],dtype={0:int}) #,nrows=40
    df_each=pd.read_csv(path_each,sep="=",skiprows=lambda x:x<=row_start or x>=row_end+1,header=0,usecols=[1],dtype={0:int})
    #print(df_each)
    #不断合并dataframe
    df_temp=pd.concat([df_temp,df_each],axis=1,join='outer',ignore_index=True)
    #print(df_temp)

#print(df_temp)

#print(df_temp[0].dtypes)

save_path=r'D:\Study\CPK_Automate_Tool\Result.xlsx'
df_temp.to_excel(save_path,header=False,index=False)




'''
#文件保存路径
save_path=r'D:\Study\CPK_Automate_Tool\Result.csv'
#执行文件报告，不需要行索引和列索引
df_temp.to_csv(save_path,header=0,index=0)

'''


'''
'''
#方法一：获取指定目录下符合条件文件的路径
#TXT文件路径字符串-*通配符：所有TXT文件
path = r"D:\Study\CPK_Automate_Tool\test\*.txt"
#将符合路径条件的TXT文件路径生成列表文件
all_file_path=glob.glob(path)
#print(all_file_path)
'''
'''

