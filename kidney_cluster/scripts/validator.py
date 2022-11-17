from sklearn.metrics import silhouette_score, pairwise_distances,davies_bouldin_score
from sklearn.metrics.cluster import adjusted_rand_score, normalized_mutual_info_score
from validclust import dunn
from scipy import stats

import pandas as pd
import math

def silhouette(data, labels):
   return silhouette_score(data,labels)

def dunn(data, labels):
   dist = pairwise_distances(data)
   return dunn(dist, labels)

def dbi(data,labels):
   return davies_bouldin_score(data, labels)

def ari(labels_true, labels_predict):
   return adjusted_rand_score(labels_true, labels_predict)

def nmi(labels_true, labels_predict):
   return normalized_mutual_info_score(labels_true, labels_predict)

def run_tTest(samplesA, samplesB, alpha = 0.05):
   statistic,p_value = stats.ttest_ind(samplesA,samplesB)
   if p_value < alpha:
      print("p-value(%.4f) < alpha(%.2f)\nThere is enough statistical evidence that two samples have significant difference." % (p_value, alpha))
   else:
      print("p-value(%.4f) > alpha(%.2f)\nThere is not enough statistical evidence that two samples have significant difference." % (p_value, alpha))
   return   

def compute_entropy(label2predict, label2mix):
   data = pd.DataFrame()
   data["label2predict"] = label2predict
   data["label2mix"] = label2mix
   entropy = 0
   total_number = len(data["label2predict"])
   for center in pd.unique(data["label2predict"]):
      cluster_entropy = 0
      data_cluster = data[data["label2predict"] == center]
      memberNum = len(data_cluster)
      count_series = data_cluster["label2mix"].value_counts()
      for i in range(0, len(count_series)):
         probability = count_series.iloc[i]/memberNum
         cluster_entropy += probability * math.log2(probability)
      entropy += -(cluster_entropy) * (memberNum/total_number)
   return entropy

def compute_baseline_entropy(label2predict, label2mix):
   data = pd.DataFrame()
   entropy = 0
   data["label2predict"] = label2predict
   data["label2mix"] = label2mix
   total_number = len(data["label2predict"])
   
   for center in pd.unique(data["label2predict"]):
      cluster_entropy = 0
      data_cluster = data[data["label2predict"] == center]
      memberNum = len(data_cluster)
      for i in range(0, len(set(data["label2mix"].to_list()))):
         probability = 1 / len(set(data["label2mix"].to_list()))
         cluster_entropy += probability * math.log2(probability)
         entropy += -(cluster_entropy) * (memberNum/total_number)
   return entropy