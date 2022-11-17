2022-06-10 00:19:17.094577: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-10 00:19:17.094610: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/crowding_tuning.py", line 82, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/crowding_tuning.py", line 68, in main
    ga = run_ga(data, center, eta)
TypeError: run_ga() missing 2 required positional arguments: 'mutPb' and 'cxPb'
