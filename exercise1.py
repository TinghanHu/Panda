import pandas as pd

Series1 = pd.Series([100, 200, 300, 400, 500], index=['A', 'B', 'C', 'D', 'E'])
Series2 = Series1 * 2

print("Series1 的內容:")
print(Series1)
print("\nSeries2 的內容:")
print(Series2)