2022-06-10 00:21:44.718233: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-10 00:21:44.718263: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/crowding_tuning.py", line 82, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/crowding_tuning.py", line 75, in main
    plt.savefig(fileName)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/pyplot.py", line 958, in savefig
    res = fig.savefig(*args, **kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/figure.py", line 3019, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/backend_bases.py", line 2319, in print_figure
    result = print_method(
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/backend_bases.py", line 1648, in wrapper
    return func(*args, **kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/_api/deprecation.py", line 412, in wrapper
    return func(*inner_args, **inner_kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/backends/backend_agg.py", line 541, in print_png
    mpl.image.imsave(
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/matplotlib/image.py", line 1675, in imsave
    image.save(fname, **pil_kwargs)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/PIL/Image.py", line 2209, in save
    fp = builtins.open(filename, "w+b")
OSError: [Errno 28] No space left on device: '/deac/csc/khuriGrp/zhaok220/clustering/output/crowding_tuning/crowding_convergence_analysis_house16H/crowding=0.020000.png'
