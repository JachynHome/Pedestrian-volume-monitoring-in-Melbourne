import pandas as pd

f=pd.read_csv("2012_03-HOUR.CSV")
for i in f:
    print(i)
print(len(f))
i=0
while i< len(f):
    print(f[i])


