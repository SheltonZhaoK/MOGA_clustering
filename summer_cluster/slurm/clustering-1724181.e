Traceback (most recent call last):
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/deac/generalGrp/khuriGrp/software/python/3.8.10/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/scoop/__main__.py", line 21, in <module>
    main()
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/scoop/launcher.py", line 464, in main
    args.external_hostname = [utils.externalHostname(hosts)]
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/scoop/utils.py", line 95, in externalHostname
    hostname = hosts[0][0]
IndexError: list index out of range
