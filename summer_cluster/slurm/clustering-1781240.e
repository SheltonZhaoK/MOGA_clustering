2022-07-15 18:26:59.619743: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-15 18:26:59.619776: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 31, in <module>
    main(dirName, fileName, labelName)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 15, in main
    ga = run_mo_gakmeans(data,numCenters,numGen = 350, sizePop = 600)
NameError: name 'numCenters' is not defined
