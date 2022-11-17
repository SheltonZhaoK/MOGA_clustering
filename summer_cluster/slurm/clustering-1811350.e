Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/pop_iter_scrna.py", line 26, in <module>
    main(dirName,dataName)
  File "/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/pop_iter_scrna.py", line 11, in main
    data, cellId = read_scrnaseq_data(dirName+dataName)
  File "/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/reader.py", line 28, in read_scrnaseq_data
    data = pd.read_csv(filename)
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
FileNotFoundError: [Errno 2] No such file or directory: '/deac/csc/khuriGrp/zhaok220/clustering/data/scrna_benchmarks_umap/10X_NCI_M_A_cellranger3.1_umap.csv'
