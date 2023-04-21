#导入数据分析pandas库
import pandas as pd #
#导入查找文件目录和文件名的模块
import glob 
#导入系统os库
import os
#导入处理excel 文件的openpyxl库
import openpyxl


########################################   TXT PROCESS  ######################################
#选择/输出MES LOG 文件存放的根目录
path_txt=r'D:\Study\CPK_Automate_Tool\test\sub1\sub11'  #存放数据的根目录

# 获取所有文件的完整路径名
all_files_path=[]
for root,dirs,files in os.walk(path_txt,topdown=False):   #os.walk()方法，是用于遍历文件目录，并返回目录名称的方法；root 所指的是当前正在遍历的这个文件夹的本身的地址；files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)  
    if len(files)>0:  #空文件夹没有文件的无需读取
        each_foder_files=[os.path.join(root,x) for x in files] #通过目录root+文件名file,合成每个文件的路径名
        all_files_path.extend(each_foder_files)

#获取第一个TXT文件作为索引
df_temp_txt=pd.read_csv(all_files_path[0],sep="=",header=0,usecols=[0])
#print(df_temp)


#循环读取TXT文件到dataframe数据结构中
for path_each in all_files_path:
    #每个文件读取为1个dataframe
    df_each_txt=pd.read_csv(path_each,sep="=",header=0,usecols=[1])
    #不断合并dataframe
    df_temp_txt=pd.concat([df_temp_txt,df_each_txt],axis=1,join='outer',ignore_index=True)



##################################  CSV  PROCESS  ################################


 #存放CSV目标文件的路径
path_csv=r'D:\Study\CPK_Automate_Tool\FQ29PB007F-20230131_104334_NSFT_PASS.csv' 

#读取一个CSV文件到dataframe
#指定行索引为TEST 列，以便下一步获取行号
df_temp_csv=pd.read_csv(path_csv,header=0)  #,index_col='TEST'


####################################  筛选数据   #############################

#使用正则表达式筛选出TXT文件满足需求的行
df_temp_txt_SN=df_temp_txt[df_temp_txt[2].str.match(r'[A-Z][0-9A-Z]{9}',na=False)].head(1)#筛选出SN项，10位数字及大写字母字符串，第一位为大写字母  #na=False的意思就是，遇到非字符串的情况，直接忽略。你也可以写na=True，意思就是遇到非字符串的情况，计为筛选有效；考虑到有可能匹配到多行，head(1)只选择第一行
df_temp_txt_IMEI=df_temp_txt[df_temp_txt[2].str.match(r'\b[0-9]{15}$',na=False)].head(1)#筛选出IMEI项，15位数字型字符串;   考虑到有可能匹配到多行，head(1)只选择第一行
df_temp_txt_NUM=df_temp_txt[df_temp_txt[2].str.match(r'[-]*\d{1,4}[.]?\d{0,5}$\b',na=False)]  #筛选出纯数值的测试项，模式主要有 -xx.xx;xx;xx.xx
df_temp_txt_target=pd.concat([df_temp_txt_SN,df_temp_txt_IMEI,df_temp_txt_NUM],axis=0,join='outer',ignore_index=True)



#使用正则表达式筛选出CSV文件满足需求的行
df_temp_csv_SN=df_temp_csv[df_temp_csv['VALUE'].str.match(r'[A-Z][0-9A-Z]{9}',na=False)].head(1)#筛选出SN项，10位数字及大写字母字符串，第一位为大写字母  #na=False的意思就是，遇到非字符串的情况，直接忽略。你也可以写na=True，意思就是遇到非字符串的情况，计为筛选有效；考虑到有可能匹配到多行，head(1)只选择第一行
print(df_temp_csv_SN)
df_temp_csv_IMEI=df_temp_csv[df_temp_csv['VALUE'].str.match(r'\b[0-9]{15}$',na=False)].head(1)#筛选出IMEI项，15位数字型字符串;   考虑到有可能匹配到多行，head(1)只选择第一行
print(df_temp_csv_IMEI)
df_temp_csv_NUM=df_temp_csv[df_temp_csv['VALUE'].str.match(r'[-]*\d{1,4}[.]?\d{0,5}$\b',na=False)]  #筛选出纯数值的测试项，模式主要有 -xx.xx;xx;xx.xx
print(df_temp_csv_NUM)
df_temp_csv_target=pd.concat([df_temp_csv_SN,df_temp_csv_IMEI,df_temp_csv_NUM],axis=0,join='outer',ignore_index=True)
print(df_temp_csv_target)



"""
#保存文件
save_path=r'D:\Study\CPK_Automate_Tool\Result_All.xlsx'  #保存文件的路径及文件名
writer=pd.ExcelWriter(save_path)  #创建一个Writer 对象
df_temp_txt.to_excel(excel_writer=writer,index=False,sheet_name='TXT_DATA') #保存原始TXT到sheet表
df_temp_csv.to_excel(excel_writer=writer,index=False,sheet_name='CSV_DATA')#保存原始CSV到sheet表
df_temp_txt_target.to_excel(excel_writer=writer,index=False,sheet_name='TXT_TARGET') #保存经过筛选的TXT到sheet表
writer.save()

"""
