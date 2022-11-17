library(scrnabench)
dataDir = '/deac/csc/khuriGrp/zhaok220/clustering/data'
outputDir = "/deac/csc/khuriGrp/zhaok220/clustering/data/scrna_benchmarks_tsne"
datasets = data_load(path = dataDir)
#datasets = data_load(demo = T)
dataList = extract_datasets(datasets)
dataList = preprocess(dataList)
dataList = annotate_datasets(dataList)
dataList = run_log(dataList)
dataList = select_hvg(dataList)
dataList = scale_data(dataList)
dataList = run_pca(dataList, numComponents = 10)
#dataList = run_umap(dataList, numDimensions = 10)
dataList = run_tsne(dataList, numDimensions = 10)
names = names(dataList)
for (i in 1:length(names))
{
   print(i)
   data = Seurat::Embeddings(dataList[[i]],'tsne')
   file = paste(outputDir,"/" ,names[i],"_tsne.csv", sep= "")
   write.csv(data,file, row.names = TRUE)
}

