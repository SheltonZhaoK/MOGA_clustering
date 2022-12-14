from sklearn.metrics import silhouette_score, pairwise_distances,davies_bouldin_score
from validclust import dunn
from scipy import stats

def silhouette(data, labels):
   return silhouette_score(data,labels)

def dunn(data, labels):
   dist = pairwise_distances(data)
   return dunn(dist, labels)

def dbi(data,labels):
   return davies_bouldin_score(data, labels)

def run_tTest(samplesA, samplesB, alpha = 0.05):
   statistic,p_value = stats.ttest_ind(samplesA,samplesB)
   if p_value < alpha:
      print("p-value(%.4f) < alpha(%.2f)\nThere is enough statistical evidence that two samples have significant difference." % (p_value, alpha))
   else:
      print("p-value(%.4f) > alpha(%.2f)\nThere is not enough statistical evidence that two samples have significant difference." % (p_value, alpha))
   return   
