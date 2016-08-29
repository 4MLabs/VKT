# VKT
VNC Killer Tool - Kills VNC windows process


Kills a VNC instance running on a Windows system.

It doesn't need any arguments, it scans automaticaly the VNC instance and kills it.

EXE file works fine in environments without the Python interpreter.

### Building

To buid the executable just type in console as follows:

```
pyinstaller -i <iconfile>.ico -onefile vnckiller.py
```

Of course you must have installed pyinstaller. If you don't just type:

```
pip install pyinstaller
```
