@echo off
setlocal enabledelayedexpansion

set "imageName=image: muhammadtabish/bankist-app"
set "newTag=v1"

set "file=kustomize\deployment.yml"

for /f "delims=" %%i in ('type "%file%"') do (
    set "line=%%i"
    set "line=!line:~0,13!!line:~22!"
    if not "!line!"=="%imageName%" (
        echo !line!>>"%file%.tmp"
    ) else (
        echo %imageName%:%newTag%  # Replace with your Docker image and tag>>"%file%.tmp"
    )
)

del "%file%"
rename "%file%.tmp" "%file%"

endlocal
