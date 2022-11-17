import pandas as pd
from clusterer import *
from validator import *
from visualizer import *
def check_clusters_data_points(memberships):
   cluster_count = []
   cluster_id = set(memberships)
   for cluster in cluster_id:
      cluster_count.append(memberships.count(cluster))
   return cluster_count

def post_transformation(data, numDatasets):
   k_data =  run_kmeans(data, numDatasets)
   k_data.assign_memberships(data)
   memberships = k_data.memberships
   centers = k_data.centers

   centerPoint = [0,0]
   transformation = []
   for center in centers:
      distance = [center[0]-centerPoint[0], center[1]-centerPoint[1]]
      transformation.append(distance)
   data = data.values.tolist()
   for i in range(0, len(data)):
      data[i] = [data[i][0] - transformation[memberships[i]][0], data[i][1] - transformation[memberships[i]][1]]
   data = pd.DataFrame(data)
   return data

def main(dataDir, numDatasets):
   data = dataDir + 'intergration_without_harmony.csv'
   data_harmony = dataDir + 'intergration_with_harmony.csv'

   data_anotation = pd.read_csv(data)
   data_harmony_anotation = pd.read_csv(data_harmony)
  
   data_values = data_anotation[['UMAP_1','UMAP_2']]
   data_harmony_values = data_harmony_anotation[['UMAP_1','UMAP_2']]
   
   print('\nk = 10') 
   print("Sil_x_harmony: %.2f" % (silhouette(data_values, data_anotation['clusters'].tolist())))
   print("Sil_harmony: %.2f" % (silhouette(data_harmony_values, data_harmony_anotation['clusters'].tolist())))

   k_data = run_kmeans(data_values, numDatasets)
   k_data.assign_memberships(data_values)

   k_harmony = run_kmeans(data_harmony_values,numDatasets)
   k_harmony.assign_memberships(data_harmony_values)

   print('\nk = ' + str(numDatasets))
   print("Sil_x_harmony: %.2f" % (silhouette(data_values, k_data.memberships)))
   print("Sil_harmony: %.2f" % (silhouette(data_harmony_values, k_harmony.memberships)))
   print("x_harmony_clusters data counts: " + str(check_clusters_data_points(k_data.memberships)))
   print("harmony_clusters data counts: " + str(check_clusters_data_points(k_harmony.memberships)))
   
   #post transformation
   data_trans = post_transformation(data_values, numDatasets)
   plot_data(data_trans,'/deac/csc/khuriGrp/zhaok220/data_intergration/output/data_trans.png')
   data_harmony_trans = post_transformation(data_harmony_values, numDatasets)
   plot_data(data_trans,'/deac/csc/khuriGrp/zhaok220/data_intergration/output/data_harmony_trans')
   
   k_data = run_kmeans(data_trans, 10)
   k_data.assign_memberships(data_trans)

   k_harmony = run_kmeans(data_harmony_trans,10)
   k_harmony.assign_memberships(data_harmony_trans)
   
   print('\n###After transformation###')
   print('k = 10') 
   print("Sil_x_harmony: %.2f" % (silhouette(data_trans, k_data.memberships)))
   print("Sil_harmony: %.2f" % (silhouette(data_harmony_trans, k_harmony.memberships )))
   
   print(data_trans)
   print(data_harmony_trans)
if __name__ == '__main__':
   dataDir = '/deac/csc/khuriGrp/zhaok220/data_intergration/data/'
   numDatasets = 4
   main(dataDir, numDatasets)
