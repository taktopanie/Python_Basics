from cx_Freeze import setup, Executable


exe = Executable(script="my_app.pyw",

                 base="Win32GUI",

                 icon="my_app.ico",

                 compress=True,

                 appendScriptToExe=True,

                 appendScriptToLibrary=False,

                 copyDependentFiles=True)


setup(name="MyApp",

      version="1.0",

      description="This is my first app",

      author="dp",

      author_email="dp@example.com",

      executables=[exe],

      options={'build_exe': {'excludes': ['tcl', 'ttk', 'tkinter'],

                             'packages': [],

                             'include_files': ['license.txt'],

                             'compressed': True,

                             'create_shared_zip': False}})
