import os
import pandas as pd
import numpy as np

'''
Maximum
'''
'''
results = pd.DataFrame()
for i in range (1, 7):
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/metamorphic_test/MOEA/'+str(i)
   for data in os.listdir(dirName):
      datas = [[],[],[]]
      maxs = [[],[],[]]
      df = pd.DataFrame()
      dataDir = dirName + '/'+ data
      
      df = pd.read_csv(dataDir)
      datas[0].append(df["ga-sw"].tolist())
      datas[1].append(df["k-sw"].tolist())
      datas[2].append(df["phg-sw"].tolist())

   print(len(datas[0]))
   for i in range(0, len(datas)):
      datas[i] = np.array(datas[i]).T.tolist()

   for i in range(0, len(datas)):
      for j in range(0, len(datas[0])):
         maxs[i].append(max(datas[i][j]))

   df["ga-sw"] = maxs[0]
   df["k-sw"] = maxs[1]
   df["phg-sw"] = maxs[2]
   del df['Unnamed: 0']
   print(df)
results.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/metamorphic_test_moea.csv')
'''

'''
Average
'''

results = pd.DataFrame()
for z in range (0, 1):
   #dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/metamorphic_test/MOEA/'+str(z)
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/results1_2/scrna_mul_run_so'
   datas = [[],[],[]]
   means = [[],[],[]]
   df = pd.DataFrame()

   for data in os.listdir(dirName):
      dataDir = dirName + '/'+ data
      
      df = pd.read_csv(dataDir)
      datas[0].append(df["ga-sw"].tolist())
      datas[1].append(df["k-sw"].tolist())
      datas[2].append(df["phg-sw"].tolist())
   pd.DataFrame(datas[0]).to_csv('../output/so_convergence.csv')
   for i in range(0, len(datas)):
      datas[i] = pd.DataFrame(datas[i]).T.values.tolist()

   print(pd.DataFrame(datas[0]))
   for i in range(0, len(datas)):
      for j in range(0, len(datas[0])):
         means[i].append(sum(datas[i][j])/len(datas[i][j]))
   
   df["ga-sw"] = means[0]
   df["k-sw"] = means[1]
   df["phg-sw"] = means[2]
   del df['Unnamed: 0']
   if len(results) == 0:
      results['MR0'] = df["ga-sw"].tolist()
   else:
      name = 'MR'+str(z)
      results.insert(len(results.iloc[0]),name, df["ga-sw"].tolist())
results.index = df.index.tolist()       
#results.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/metamorphic_test/metamorphic_test_moea.csv')
print(results)


'''
for z in range (0, 1):
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/time_comparison/SO_speedUp'
   datas = [[]]
   means = [[]]
   df = pd.DataFrame()

   for data in os.listdir(dirName):
      dataDir = dirName + '/'+ data
      
      df = pd.read_csv(dataDir)
      datas[0].append(df["so-time"].tolist())

   for i in range(0, len(datas)):
      datas[i] = pd.DataFrame(datas[i]).T.values.tolist()

   for i in range(0, len(datas)):
      for j in range(0, len(datas[0])):
         means[i].append(sum(datas[i][j])/len(datas[i][j]))

results = pd.DataFrame()
results['Instance #'] = df['Instance #']
results['so-time'] = means[0]
results.index = df['Benchmark']       
results.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/time_comparison_so_mean.csv')

print(results)
'''

'''
aggregate
'''
'''
dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/synthetic_data/1_7'
results = pd.DataFrame() 
for data in os.listdir(dirName):
   dataDir = dirName + '/'+ data
   df = pd.read_csv(dataDir)
   results = results.append(df)
del results['Unnamed: 0']
results.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/synthetic_1_7_aggregate.csv')
print(results)   
'''

'''
Average
'''
'''
#dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/synthetic_data/1-7'
names = ['1_32','32_1','16_2','2_16','4_8','8_4']
for name in names:
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/time_comparison/' + name
   results = pd.DataFrame()
   for data in os.listdir(dirName):
      dataDir = dirName + '/'+ data
      df = pd.read_csv(dataDir)
      del df['Benchmark']
      results = results.add(df, fill_value = 0)
   results = results.div(len(os.listdir(dirName)))
   print(results)
   results.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/time_comparison_MO_'+name+'mean.csv')
   
'''
'''
maximum
'''
'''
dirName = '/deac/csc/khuriGrp/zhaok220/clustering/output/synthetic_data/1_7'

datas = [[] for _ in range(0,22)]
maxs = [[] for _ in range(0,22)]

df = pd.DataFrame()
for data in os.listdir(dirName):
   dataDir = dirName + '/'+ data
   df = pd.read_csv(dataDir)
   
   for i in range (0, len(df.iloc[0])):
      datas[i].append(df.iloc[:,i].tolist())
   
for i in range(0, len(datas)):
   datas[i] = pd.DataFrame(datas[i]).T.values.tolist()

for i in range(0, len(datas)):
   for j in range(0, len(datas[0])):
      maxs[i].append(max(datas[i][j]))

for i in range (0, len(df.iloc[0])):
   df.iloc[:,i] = maxs[i]

print(df)
df.to_csv('../output/synthetic_1_7_max.csv')
'''
