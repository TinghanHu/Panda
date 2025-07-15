import pandas as pd

data = {
    'IP': 95,
    'Physics': 89,
    'Chemistry': 92,
    'Math': 95
}

s = pd.Series(data)

print("Display all subjects:")
print(s)
print("-" * 30) 

ip_marks = s['IP']
print("Display only IP:")
print(ip_marks)
print("-" * 30)

s_increased = s + 10

print(" Increase marks of all subjects by 10:")
print(s_increased)