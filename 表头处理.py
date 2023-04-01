import pandas as pd 

filepath="D:\学习\CPK自动化工具\data\FQ29PB007A-20230131_105159_NSFT_PASS.csv"  #文件路径
file = pd.read_csv(filepath,header=0,index_col='TEST')   #hearder=0--选第一行作为列索引；index_col='TEST'--选“TEST”列作为行索引
#print(file)
file1=file[['L_LIMIT','U_LIMIT']]  #选择上限"L_LIMIT"和下限“U_LIMIT”两列
#print(file1)
file_title=file1.T  #转置,得到常规表头
#print(file_title)  
file_title.to_excel('D:\学习\CPK自动化工具\data\CPK_title.xlsx')  #表头写到EXCEL表
