import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Převod_měn 2.0",
    version="2.0",
    description="Upgrade aplikace za pomoci PyQt místo tkinter",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="img/icon.ico")]
)