#本程序为了准确截取MES TXT LOG 中所需的数据

import pandas as pd

 #存放MES LOG TXT目标文件的路径
path=r'D:\Study\CPK_Automate_Tool\test\FQ29PB006J-20230130_203239_NSFT_PASS.txt' 

#读取一个MES LOG TXT文件到dataframe
df_temp=pd.read_csv(path,sep="=") 
print(df_temp)

#获取dataframe中标志为[TEST_DATA]及[TEST_RESULT]的行号，因为所需数据在两个标志之间
row_start=df_temp.index.get_loc('[TEST_DATA]')
row_end=df_temp.index.get_loc('[TEST_RESULT]')
print(row_start)
print(row_end)

#截取[TEST_DATA]及[TEST_RESULT]两个标志之间的数据到dataframe
df_temp=pd.read_csv(path,sep="=",skiprows=lambda x:x<=row_start or x>=row_end+1)  #,nrows=40  ,header=3,usecols=[1],dtype={0:int} skip_blank_lines=True
print(df_temp)