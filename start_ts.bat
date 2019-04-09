@echo off
SET PATH=C:\Soft\Anaconda3;C:\Soft\Anaconda3\Scripts;C:\Soft\Anaconda3\Library\bin;%PATH%
call activate tests
REM python -m ipykernel install --user --name tensorflow --display-name "Python (tensorflow)"
jupyter notebook