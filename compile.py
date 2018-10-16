from distutils.core import setup
import py2exe

setup(options = {"py2exe": {"includes": ["tkinter"]}},
       console=["run.py"])
