@ECHO OFF
CLS
:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2, 3, 4 or 5 to select your task
ECHO ...............................................
ECHO.
ECHO 1 - Install Env
ECHO 2 - Update Env
ECHO 3 - Compile
ECHO 4 - Run Botpd
Echo 5 - Exit
ECHO.
SET /P M=Type 1, 2, 3, 4 or 5 then press ENTER:
IF %M%==1 GOTO INSTALL
IF %M%==2 GOTO UPDATE

IF %M%==3 GOTO COMPILE
IF %M%==4 GOTO RUN
IF %M%==5 GOTO EXIT
:INSTALL
start cmd /c conda env create -f environment.yml
GOTO MENU
:UPDATE
start cmd /c conda env update -f environment.yml
GOTO MENU
:COMPILE
python ./build.py
GOTO MENU
:RUN
conda activate botpd && python src/main.py
GOTO MENU
:EXIT
EXIT
