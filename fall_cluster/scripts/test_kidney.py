import sys
from reader import *
from new_clusterer import *
from validator import *
from preprocesser import *
from reader import *
def main(dirName,fileName,labelName,label2predict):
   result = pd.DataFrame(columns = ['instance #','labels #','moea-time','soea-time','moea-sil','moea-ARI','moea-NMI','soea-sil','soea-ARI',\
'soea-NMI','kmeans-sil','kmeasn-ARI','kmeans-NMI','phe-sil','phe-ARI','phe-NMI'])

   data, cellId = read_scrnaseq_data(dirName + fileName)   
   labels = pd.read_csv(dirName + labelName)
   
   label = labels[label2predict].astype('category').cat.codes.tolist()
   numClusters = len(set(label))
   print(numClusters)   
   moea = run_mo_gakmeans(data,numClusters,numGen = 350, sizePop = 600)
   moea.assign_memberships(data)
   print('moea done')  
   soea = run_so_gakmeans(data,numClusters,numGen = 350, sizePop = 600)
   soea.assign_memberships(data)
   print('soea done')
   pheMemberships = run_phenograph(data)
   
   kmeans = run_kmeans(data, numClusters, 350)
   kmeans.assign_memberships(data)
 
   sil = [silhouette(data, moea.memberships), silhouette(data, soea.memberships), silhouette(data, kmeans.memberships), silhouette(data, pheMemberships)]
   NMI = [nmi(label, moea.memberships), nmi(label, soea.memberships), nmi(label, kmeans.memberships), nmi(label, pheMemberships)]
   ARI = [ari(label, moea.memberships), ari(label, soea.memberships), ari(label, kmeans.memberships), ari(label, pheMemberships)]
  
   tempt = [len(data), numClusters, "{:.3f}".format(moea.time), "{:.3f}".format(soea.time)] 
   for j in range (0, len(sil)):
      tempt.extend(["{:.3f}".format(sil[j]), "{:.3f}".format(ARI[j]), "{:.3f}".format(NMI[j])])

   result.loc[0] = tempt
   
   labels = data
   labels['MOEA'] = moea.memberships
   labels['SOEA'] = soea.memberships
   labels['PhenoGraph'] = pheMemberships
   
   name = '../output/kidney_clusters_'+label2predict+'.csv'
   labels.to_csv(name)
   name = '../output/results_kidney_' + label2predict+'.csv'
   result.to_csv(name) 
       
if __name__ == '__main__':
   dirName = '../data/kidney/'
   fileName = 'pca_umap.csv'
   labelName = 'labels.csv'
   label2predict = sys.argv[1]
   main(dirName, fileName, labelName, label2predict)
   
