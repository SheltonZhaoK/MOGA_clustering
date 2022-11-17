2022-06-30 14:51:22.624174: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-30 14:51:22.624213: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel.py", line 116, in <module>
    main(dirName)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel.py", line 97, in main
    ga = run_mo_gakmeans(data,numCenters,numGen = 2, sizePop = 2)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/clusterer.py", line 221, in run_mo_gakmeans
    offspring = toolbox.tourSelect(pop, len(pop))
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/deap/tools/selection.py", line 68, in selTournament
    chosen.append(max(aspirants, key=attrgetter(fit_attr)))
ValueError: max() arg is an empty sequence
