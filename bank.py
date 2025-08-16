import pandas as pd

# 讀取 Excel 檔案中的第一個頁籤（客戶基本資訊）
customers_df = pd.read_excel('bank_data.xlsx', sheet_name='customers_info', skiprows=1, # 跳過第一行
    header=0)   # 將第二行設為表頭)

# 讀取 Excel 檔案中的第二個頁籤（交易記錄）
transactions_df = pd.read_excel('bank_data.xlsx', sheet_name='transactions', skiprows=1, # 跳過第一行
    header=0)   # 將第二行設為表頭)

# # 使用 merge() 函式進行合併
matched_data = pd.merge(customers_df, transactions_df, on='CustomerID', how='inner')
matched_data['Account'] = matched_data['Account'].astype(str) + '0'
# # 印出結果
# print("有最新交易紀錄的客戶資料：")
print(matched_data)
# print(customers_df)
# print(transactions_df)