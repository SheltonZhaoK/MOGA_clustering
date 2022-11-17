2022-08-17 23:59:09.703805: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-08-17 23:59:09.703873: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
/deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_kidney.py:12: DtypeWarning: Columns (12,13,14) have mixed types. Specify dtype option on import or set low_memory=False.
  labels = pd.read_csv(dirName + labelName)
/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/deap/creator.py:138: RuntimeWarning: A class named 'Individual' has already been created and it will be overwritten. Consider deleting previous creation of that class or rename it.
  warnings.warn("A class named '{0}' has already been created and it "
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_kidney.py", line 53, in <module>
    main(dirName, fileName, labelName, label2predict)
  File "/deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_kidney.py", line 34, in main
    tempt.extend(["{:.3f}".format(sil[j]), "{:.3f}".format(ARI[j]), "{:.3f}".format(NMI[j])])
IndexError: list index out of range
