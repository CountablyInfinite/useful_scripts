# useful_scripts
A collection of useful and (mostly) hacky scripts to get work done.

 - **resize_images:** Python script to resize all images inside the current folder to 1/2 of the original size and export it to ./resized as .jpg in 80% quality. 
 The binary has been built with pyinstaller to run on 64-Bit Windows systems.
 ```pyinstaller --onefile --icon=youricon.ico pythonfile.py```