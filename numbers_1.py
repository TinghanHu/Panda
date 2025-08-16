import pandas as pd
df = pd.read_excel(
    'student_scores.xlsx',
    header=1,  # 將 header 設為 1，表示第2行就是表頭
    skiprows=1,  # 跳過第一行
    
)

print("原始學生分數資料：")
print(df)

# 計算每科的平均分數
average_scores = df[['Math', 'English', 'Science']].mean()

# 印出結果
print("\n各科的平均分數：")
print(average_scores)

# 篩選數學成績高於 85 的學生
high_math_scores = df[df['Math'] > 85]

print("數學成績高於 85 分的學生：")
print(high_math_scores)
# 計算每個學生的總分
df['Total'] = df['Math'] + df['English'] + df['Science']

# 計算每個學生的平均分數
df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1)

print("新增總分和平均分數欄位後的資料：")
print(df)
