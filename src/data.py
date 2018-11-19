"""
1-workload type:
    A,B,C,D,E
2-contention:
    contender:1,victim:2,independ:3
3-contention type
    No:0 LLC:1 MB:2 UNKNOWN:3
rules:
    one contender,others are vicitims e.g [A1, B2, C2] 1
    all independent,no victimis and contenders e.g [A3, B3, C3] 0
"""

import numpy as np
import pandas as pd
import datetime

print("Start generate data",datetime.datetime.now())

a = []
for i in range(1000):# as large as you can
    for length in range(1,6): # len of cluster 1,2,3,4,5
        
        if length == 2:
            for k in range(2):
                r = np.random.choice(['A','B','C','D'],size = length,replace= False)
                a.append(sorted(r))
        if length == 3 or length == 4:
            for k in range(4):
                r = np.random.choice(['A','B','C','D','E'],size = length,replace= False)
                a.append(sorted(r))
        if length == 1:
            for k in range(1):
                r = np.random.choice(['A','B','D'],size = length,replace= False)
                a.append(sorted(r))
        if length == 5:
            for k in range(1):
                r = np.random.choice(['A','B','C','D','E','F'],size = length,replace= False)
                a.append(sorted(r))


np.random.shuffle(a)
print('Shuffle The Data')


trans = [] #with both contentions and non-contentions
trans_type = []
trans_c = [] #only contentions
trans_c_type = []

for item in a:
    new_item = []

    choice = np.random.choice([True,False],size = 1,replace = False,p=[0.1,0.9])
    if choice[0] == False:
        for v in item:
            new_item.append(v+'3')
        trans.append(new_item)
        trans_type.append(0) # 0 means no contention
    else:
        length = len(item)
        ch = np.random.choice( [x for x in range(length)] ,size = 1,replace = False)
        for i,v in enumerate(item):
            if i == ch[0]:
                new_item.append(v+'1')
            else:
                new_item.append(v+'2')
        
        trans.append(new_item)
        trans_c.append(new_item)
        tp = np.random.choice( [x for x in [1,2,3]] ,size = 1,replace = False) #[1,2,3] is the contention type
        trans_type.append(tp[0])
        trans_c_type.append(tp[0])
"""
all_df = pd.DataFrame(trans)
all_df.to_csv("data/data.csv",header = None, index=False)
sub_df = pd.DataFrame(trans_c)
sub_df.to_csv("data/data_c.csv",header = None, index=False)
"""

pd_df = pd.DataFrame({"trans":trans,"type":trans_type})
pd_df.to_csv("data/data_pd.csv", index=False)
pd_df_c = pd.DataFrame({"trans":trans_c,"type":trans_c_type})
pd_df_c.to_csv("data/data_pd_c.csv", index=False)

with open('data/data.txt','w') as out:
    for tran in trans:
        for index,item in enumerate(tran):
            if index != len(tran)-1:
                out.write(str(item)+'\t')
            else:
                out.write(str(item))
        out.write('\n')
with open('data/data_c.txt','w') as out:
    for tran in trans_c:
        for index,item in enumerate(tran):
            if index != len(tran)-1:
                out.write(str(item)+'\t')
            else:
                out.write(str(item))
        out.write('\n')

print("End generate data",datetime.datetime.now())
