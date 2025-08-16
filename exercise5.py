import pandas as pd

# 1. 定義 Series 的資料值
# 這些是你要顯示的數值。
val1 = [50000, 65890, 56780, 89000, 77900]
index_labels = ['QTR1', 'QTR2', 'QTR3', 'QTR4', 'QTR5']

SQTR = pd.Series(val1, index=index_labels)

print("SQTR Series 的內容如下：")
print(SQTR)
