import pandas as pd

data_values = [700, 700, 700, 700, 700]

index_labels = [200, 201, 202, 203, 204]

Series1 = pd.Series(data_values, index=index_labels)


print("創建的 Series1 內容如下：")
print(Series1)