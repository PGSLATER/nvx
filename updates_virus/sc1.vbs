Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "upload and run bat"
WshShell.Run "pythonw.exe script1.py", 0, False
Set WshShell = Nothing
