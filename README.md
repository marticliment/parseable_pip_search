# parse_pip_search

__Wrapping the needs of a "pip search" command necessity through PyPi.org, on a command-line parseable output__

## Installation & Usage
Install with `pip install parse_pip_search`

Use with `parse_pip_search anything`

You can specify sorting options : 
- `parse_pip_search -s name`
- `parse_pip_search -s version`
- `parse_pip_search -s released`

Example:
```
C:\Users\user>parse_pip_search win32
 Package | Version | Description
---------------------------------
win-nic|2.0.1|Python package to interface with network intetrface cards (NICs) on Windows-based computers.
win32core|221.36|Python for Window Extensions
win32-details|0.5.0|.exe file details for your Nautilus file browser
neofetch-win|1.3.3|neofetch, but for Windows
pywigxjpf-win|1.11|Windows binary wheels for pywigxjpf
win32build2|0.0.3|A small example package
livestock-win|0.0.1.dev5|Livestock is a plugin/library for Grasshopper written in Python
win7ools|0.3.0|Python project that provides programmatic access to the Windows OS
win-Auto|1.0.3|
wxbot-win|0.0.1|A wechat bot SDK for windows
toga-win32|0.1.2|A Win32 (Microsoft Windows) backend for the Toga widget toolkit.
win32compat|221.26|Python for Window Extensions
sanic-win|0.6.1|A microframework based on uvloop, httptools, and learnings of flask
pyautoit-win64|1.0.3|Python binding for AutoItX3.dll 支持64位dll
win2xcur|0.1.1|win2xcur is a tool to convert Windows .cur and .ani cursors to Xcursor format.
win32wifi|0.1.0|Python Windows Wifi - !Still Under Development!
toncli-win|0.0.4|Easy to use CLI for fift / func projects
pyenv-win|3.1.1|pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.
MultiScaleDeformableAttention-win|1.1|PyTorch Wrapper for CUDA Functions of Multi-Scale Deformable Attention
win-api|0.0.0|Collection of packages utilizing Windows API. Alias for 'https://github.com/patrikkj/winapi'.
win32-setfiletime|1.0.0|A small Python utility to set file creation/modified/accessed time on Windows
xfntr-win|0.3.1|A software that analyzes xfntr data
quantum-win32|0.0.0|
win10note|0.0|A time calculator
win32fastutils|0.1.1|Collection of win32 related utils.
win32shell|2.3|A small example package
Win32Security|2.1.0|Data secured by the Windows API
virtualenvwrapper-win|1.2.7|Port of Doug Hellmann's virtualenvwrapper to Windows batch scripts
win32ext|221.2|Python for Window Extensions
license-win|0.1.2|Library that encapsulates free software licenses
zcmds-win32|1.0.20|Cross platform(ish) productivity commands written in python.
win-cat|0.2.0|An implementation of cat for Windows
win32gui|221.6|Python for Window Extensions
sudo-win32|1.0.9|The missing sudo command for win32
win10toast|0.9|An easy-to-use Python library for displaying Windows 10 Toast Notifications
sdpc-win|3.0|a library for sdpcPY (windows version)
ffmpeg-win64|0.0.2|add ffmpeg 64bit exe builds to os.environ['PATH'] ref: https://ffmpeg.org/download.html
win10batteryoptimizer|0.1.1|An easy-to-use Python library for maintaing the optimal battery life for windows 10
trainer4win|0.0.7|General purpose model trainer for PyTorch that is more flexible than it should be, by 🐸Coqui.
win10ctypestoast|0.10|Windows-10-Toast-Notifications without pywin32 dependency

C:\Users\user>
```

## Dependencies
* bs4
* rich
* requests

## Based on [@victorgarric](https://github.com/victorgarric)'s awesome [pip_search](https://github.com/victorgarric/pip_search) utility
