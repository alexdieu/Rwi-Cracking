echo Patching ...
SET mypath=%~dp0
cd %mypath:~0,-1%
cd AppData
del "personal.ini"
echo PATCHED
