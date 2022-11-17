2022-08-29 16:08:36.950743: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-08-29 16:08:36.950783: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_synthetic_time.py", line 57, in <module>
    main(dirName, fileName, labelName, jobId, nodes, tasks, cpus)
  File "/deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_synthetic_time.py", line 13, in main
    labels = pd.read_csv(dirName + str(i) + 'k/' + labelName + str(j) + '.csv', sep = '\t',engine='python')
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1217, in _make_engine
    self.handles = get_handle(  # type: ignore[call-overload]
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/io/common.py", line 789, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '/deac/generalGrp/khuriGrp/khurin/shelton/data/data_1k/labels_1.csv'
