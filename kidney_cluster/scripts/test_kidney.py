import sys
from reader import *
from clusterer import *
from validator import *
from preprocesser import *
from reader import *

def sample_kidney(data, labels, size):
    ix = []
    for x in pd.unique(data["DID"]):
        ix.extend(data[data["DID"] == x].sample(n=size).index)
    samples = data.loc[ix].copy() 
    sam_labels = labels.loc[ix].copy() 
    return samples, sam_labels
     
def main(dataName, labelName, label2predict, label2mix):
    numGen = 350 #fixme
    sizePop = 600 #fixme
    result = pd.DataFrame(columns = ['Algorithms', 'Num_cluster','Baseline entropy','Entropy after clustering', 'Sil', 'NMI', 'ARI'])
    algorithms = ["PhenoGraph", "MOGA", "Kmeans"]

    annotation, labels = read_kidney_data(dataName, labelName, label2predict, label2mix)
    #annotation, labels = sample_kidney(annotation, labels, 5) #fixme
    labels = labels[label2predict].astype('category').cat.codes.tolist()
    baseline_entropy = compute_baseline_entropy(labels, annotation[label2mix].to_list())

    #PhenoGraph
    memberships = run_phenograph(annotation[["UMAP_1","UMAP_2"]])
    Sil = [silhouette(annotation[["UMAP_1","UMAP_2"]], memberships)]
    NMI = [nmi(memberships, labels)]
    ARI = [ari(memberships, labels)]
    Entropy = [compute_entropy(memberships, annotation[label2mix].to_list())]
    numCenters = len(set(memberships))

    '''
    #MOGA w/ 1 objective1
    moga = run_gaClustering(annotation[["UMAP_1","UMAP_2"]], objectives = 1 ,numCenters = numCenters, numGen = numGen, sizePop = sizePop)
    moga.assign_memberships(annotation[["UMAP_1","UMAP_2"]])

    Sil.append(silhouette(annotation[["UMAP_1","UMAP_2"]], moga.memberships))
    NMI.append(nmi(labels, moga.memberships))
    ARI.append(ari(labels, moga.memberships))
    Entropy.append(compute_entropy(moga.memberships, annotation[label2mix].to_list()))
    '''

    '''
    #MOGA w/ 2 objectives
    moga2 = run_gaClustering(annotation[["UMAP_1","UMAP_2"]], objectives = 2 ,numCenters = numCenters, numGen = numGen, sizePop = sizePop)
    moga2.assign_memberships(annotation[["UMAP_1","UMAP_2"]])

    Sil.append(silhouette(annotation[["UMAP_1","UMAP_2"]], moga2.memberships))
    NMI.append(nmi(labels, moga2.memberships))
    ARI.append(ari(labels, moga2.memberships))
    Entropy.append(compute_entropy(moga2.memberships, annotation[label2mix].to_list()))
   '''

    #MOGA w/ 3 objectives
    moga3 = run_gaClustering(annotation, objectives = 3 ,numCenters = numCenters, numGen = numGen, sizePop = sizePop)
    moga3.assign_memberships(annotation[["UMAP_1","UMAP_2"]])

    Sil.append(silhouette(annotation[["UMAP_1","UMAP_2"]], moga3.memberships))
    NMI.append(nmi(labels, moga3.memberships))
    ARI.append(ari(labels, moga3.memberships))
    Entropy.append(compute_entropy(moga3.memberships, annotation[label2mix].to_list()))


    #Kmeans
    kmeans = run_kmeans(annotation[["UMAP_1","UMAP_2"]], numCenters = numCenters, maxiter = numGen)
    kmeans.assign_memberships(annotation[["UMAP_1","UMAP_2"]])

    Sil.append(silhouette(annotation[["UMAP_1","UMAP_2"]], kmeans.memberships))
    NMI.append(nmi(labels, kmeans.memberships))
    ARI.append(ari(labels, kmeans.memberships))
    Entropy.append(compute_entropy(kmeans.memberships, annotation[label2mix].to_list()))

    #Output
    for i in range(0, len(algorithms)):
        result.loc[i] = [algorithms[i], numCenters, baseline_entropy, Entropy[i] , Sil[i], NMI[i], ARI[i]]
    print(result)
    result.to_csv("../output/kidney_results_comparison_ob3.csv")
    return

if __name__ == "__main__":
    dirName = '/deac/csc/khuriGrp/khurin/nathan/data/kidney/'
    dataName = dirName + 'harmonized_umap.csv'
    labelName = dirName + 'labels.csv'
    label2predict = 'STATUS'
    label2mix = 'DID'
    main(dataName, labelName, label2predict, label2mix)
