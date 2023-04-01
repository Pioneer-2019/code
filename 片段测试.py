import pandas as pd

path="D:\学习\CPK自动化工具\data\demo\FQ29PB006M-20230131_023809_NSFT_PASS.txt"
df = pd.read_csv(path,sep=None) #sep=None 表示不考虑一行中的分隔符
print(df)
print(df.T)  #转置
print(type(df))