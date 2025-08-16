import pandas as pd

S1=pd.Series(data=[31,41,51])
print(S1>40)
#只印出dat裡面大於40的值
print(S1[S1>40])
S1=pd.Series(data=[39,41,42,44], index=['A','B','C','D'])