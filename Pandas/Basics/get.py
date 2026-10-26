import pandas as pd

df = pd.DataFrame({
    "Name": ["Raj", "Amit", "Neha", "Riya", "Karan", "Priya", "Rahul", "Sneha"],
    "Age": [20, 21, 22, 23, 24, 20, 25, 22],
    "City": ["Surat", "Rajkot", "Ahmedabad", "Vadodara", "Surat", "Rajkot", "Bhavnagar", "Ahmedabad"],
    "Marks": [88, 76, 91, 67, 82, 95, 73, 89],
    "Branch": ["IT", "CE", "IT", "ME", "CE", "IT", "EC", "ME"]
    
})

print(df)
df.index =pd.RangeIndex(1, 9)
# df.index = list('ABCDEFGH')
print(df)
print(df.rename(columns={"Name":"NAME","Marks":"Score"}))
print(df)