@echo off

set py3=python3

WHERE python
IF %ERRORLEVEL% == 0 (GOTO py)
WHERE python3
IF %ERRORLEVEL% == 0 (GOTO py3)
GOTO error

:py
SET python=python
GOTO exec

:py3
SET python=python3
GOTO exec

:exec
Rem : following command is core code.
%python% manage.py migrate

%python% manage.py makemigrations sweepstake
%python% manage.py makemigrations wx_user
%python% manage.py makemigrations participate

%python% manage.py migrate
Rem : end of core code
GOTO :EOF

:error
ECHO "python utilty is required for the batch file"
GOTO :EOF