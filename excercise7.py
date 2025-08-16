import pandas as pd
S1=pd.Series(data=[39,41,42,44], index=['A','B','C','D'])
S2=pd.Series(data=10, index=['A','B','D','F'])
print(S1*S2)

#[ : 2]這是一個 Series 切片 (slicing) 的語法，類似於 Python 列表的切片。
#: 表示從開頭開始。
#2 表示到索引 2 為止，但不包含索引 2 的元素。
#因此，S1[ : 2] 會選取 S1 中索引為 0 和 1 的元素，
print(S1[ : 2]*100)

#[ : : -1] 
#: 表示從開頭開始 第二個：表示沒有指定結尾 代表整個數列 -1代表將整個數列顛倒排列
print(S2[ : : -1]*10)

