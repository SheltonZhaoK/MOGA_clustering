/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/seaborn/axisgrid.py:337: UserWarning: The `size` parameter has been renamed to `height`; please update your code.
  warnings.warn(msg, UserWarning)
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq.py", line 48, in <module>
    main(dirName)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq.py", line 36, in main
    plot_data_clustering(data,ga.memberships,numCenters,'/deac/csc/khuriGrp/zhaok220/clustering/output/scrnaseq_clustering_tsne/'+dataset+'.png')
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/visualizer.py", line 15, in plot_data_clustering
    sns.FacetGrid(data, hue="memberships", size=numCenters).map(plt.scatter, "UMAP_1", "UMAP_2").add_legend()
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/seaborn/axisgrid.py", line 700, in map
    plot_data = data_ijk[list(args)]
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/frame.py", line 3511, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 5782, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 5842, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['UMAP_1', 'UMAP_2'], dtype='object')] are in the [columns]"
