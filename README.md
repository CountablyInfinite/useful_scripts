# useful_scripts
A wild collection of useful and (mostly) hacky scripts i wrote to get different kinds of work done. Be sure you understand what you are executing before you run any of them.

- **resize_images:** Python script to resize all images inside the current folder to 1/2 of the original size and export it to ./resized as .jpg in 80% quality. 
The binary has been built with pyinstaller to run on 64-Bit Windows systems.
```pyinstaller --onefile --icon=youricon.ico pythonfile.py```

- **crypto:** A collection of scripts to demonstrate a wide variety of different techniques and algortihms used in modern cryptography.</br> -- <ins>decrypt_rsa_compare_speed.py:</ins> A script to show differences in speed when decrypting RSA with/without using the chinese rest theorem.</br> -- <ins>wieners_attack_on_rsa.py:</ins> A sample implementation of wieners attack on RSA for a small private part d.