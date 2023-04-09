#本程序为了准确截取包含测试项的 CSV LOG 中所需的数据

import pandas as pd

 #存放CSV目标文件的路径
path=r'D:\Study\CPK_Automate_Tool\FQ29PB007F-20230131_104334_NSFT_PASS.csv' 

#读取一个CSV文件到dataframe
#指定行索引为TEST 列，以便下一步获取行号
df_temp=pd.read_csv(path,index_col='TEST')  
print(df_temp)

#获取dataframe中标志为INIT_OBJECT_NSFT及UNINIT_OBJECT_NSFT的行号，因为所需数据在两个标志之间，刚好匹配MES TXT LOG中的数据
row_start=df_temp.index.get_loc('INIT_OBJECT_NSFT')
row_end=df_temp.index.get_loc('UNINIT_OBJECT_NSFT')
print(row_start)
print(row_end)

#截取及INIT_OBJECT_NSFT与UNINIT_OBJECT_NSFT两个标志之间的数据到dataframe
df_temp=pd.read_csv(path,index_col='TEST',skiprows=lambda x:x!=0 and x<=row_start or x>=row_end+2) 
print(df_temp)
