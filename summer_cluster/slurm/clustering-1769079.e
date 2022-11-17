2022-07-06 15:21:43.635080: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-06 15:21:43.635131: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 163, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_mul.py", line 63, in <module>
    main(dirName,jobId)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_mul.py", line 35, in main
    ga.assign_memberships(data)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/clusteringObject.py", line 20, in assign_memberships
    distanceList.append(dist(data[i],self.centers[j]))
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 3623, in get_loc
    raise KeyError(key) from err
KeyError: 0
