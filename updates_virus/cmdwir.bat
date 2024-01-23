@echo off
setlocal EnableDelayedExpansion

set "commandsFile=file.txt"
set "lastChecksum="

:mainLoop
REM Calculate checksum of the file
for /f %%A in ('certutil -hashfile "%commandsFile%" SHA256 ^| find /i /v "hash"') do set "checksum=%%A"

REM Check if the content has changed
if not !checksum! == !lastChecksum! (
    echo Content has changed. Executing commands...

    REM Read and execute commands from the file
    for /f "tokens=* usebackq" %%C in ("%commandsFile%") do (
        echo Executing: %%C
        %%C
    )

    REM Update lastChecksum with the current checksum
    set "lastChecksum=!checksum!"

    echo Commands executed. Waiting for changes...
)

REM Wait for a while (you can adjust the timeout)
timeout /nobreak /t 5 >nul

goto mainLoop
