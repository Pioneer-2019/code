#导入数据分析pandas 库
import pandas as pd
#导入正则表达式模块
import re

#存放MES LOG TXT目标文件的路径
path=r'D:\Study\CPK_Automate_Tool\test\FQ29PB006J-20230130_203239_NSFT_PASS.txt' 

#读取一个MES LOG TXT文件到dataframe
df_temp=pd.read_csv(path,sep="=") 
print(df_temp['[HEAD]'])

#使用正则表达式筛选出特定规律的行
print(df_temp[df_temp['[HEAD]'].str.match(r'[A-Z][0-9A-Z]{9}',na=False)]) #筛选出SN项，10位数字及大写字母字符串，第一位为大写字母  #na=False的意思就是，遇到非字符串的情况，直接忽略。你也可以写na=True，意思就是遇到非字符串的情况，计为筛选有效。
print(df_temp[df_temp['[HEAD]'].str.match(r'\b[0-9]{15}$',na=False)])  #筛选出IMEI项，15位数字型字符串
print(df_temp[df_temp['[HEAD]'].str.match(r'[-]*\d{1,4}[.]?\d{0,5}$\b',na=False)])  #筛选出纯数值的测试项，模式主要有 -xx.xx;xx;xx.xx