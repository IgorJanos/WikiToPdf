REM -----------------------------------
REM  Sample exporting script
REM -----------------------------------

set SRCFILE=%1
set DSTFILE=%~n1.docx

pandoc -s %SRCFILE% --lua-filter fixImages.lua -o %DSTFILE%
