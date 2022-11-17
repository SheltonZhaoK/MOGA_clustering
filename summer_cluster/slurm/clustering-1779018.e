2022-07-11 17:55:38.698233: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-11 17:55:38.698264: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_metamorphic.py", line 59, in <module>
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_metamorphic.py", line 38, in main
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/clusterer.py", line 261, in run_phenograph
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/phenograph/cluster.py", line 369, in cluster
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/phenograph/cluster.py", line 67, in sort_by_size
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/context.py", line 119, in Pool
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/pool.py", line 212, in __init__
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/pool.py", line 303, in _repopulate_pool
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/pool.py", line 326, in _repopulate_pool_static
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/process.py", line 121, in start
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/context.py", line 277, in _Popen
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/popen_fork.py", line 19, in __init__
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/multiprocessing/popen_fork.py", line 69, in _launch
OSError: [Errno 24] Too many open files
