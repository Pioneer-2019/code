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