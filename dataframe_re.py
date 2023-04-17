import pandas as pd

import re

#存放MES LOG TXT目标文件的路径
path=r'D:\Study\CPK_Automate_Tool\test\FQ29PB006J-20230130_203239_NSFT_PASS.txt' 

#读取一个MES LOG TXT文件到dataframe
df_temp=pd.read_csv(path,sep="=") 
print(df_temp)
print(df_temp['[HEAD]'])
print(df_temp[df_temp['[HEAD]'].str.contains('..FT',na=False)])  #na=False的意思就是，遇到非字符串的情况，直接忽略。你也可以写na=True，意思就是遇到非字符串的情况，计为筛选有效。
print(df_temp[df_temp['[HEAD]'].str.contains(r'[0-9A-Z]{10}',na=False)]) 
print(df_temp[df_temp['[HEAD]'].str.contains(r'\w{10}',na=False)]) 
print(df_temp[df_temp['[HEAD]'].str.contains(r'\d',na=False)]) 

print(df_temp[df_temp['[HEAD]'].str.match(r'[0-9A-Z]{10}',na=False)]) 
print(df_temp[df_temp['[HEAD]'].str.match(r'[A-Z][0-9A-Z]{9}',na=False)]) 
print(df_temp[df_temp['[HEAD]'].str.match(r'[0-9]{15}',na=False)]) 
print(df_temp[df_temp['[HEAD]'].str.match(r'[0-9]{15}[^,]',na=False)]) 
#print(df_temp[0].str)
#df_temp[df_temp[0]]