echo Patching ...
SET mypath=%~dp0
cd %mypath:~0,-1%
del "AppData"
