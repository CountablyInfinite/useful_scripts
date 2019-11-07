
# useful_scripts
A wild collection of useful and (mostly) hacky scripts i wrote to get different kinds of work done. Be sure you understand what you are executing before you run any of them.

-  **resize_images:**  </br>Python script to resize all images inside the current folder to 1/2 of the original size and export it to ./resized as .jpg in 80% quality.

The binary has been built with pyinstaller to run on 64-Bit Windows systems.</br>```pyinstaller --onefile --icon=youricon.ico pythonfile.py```

-  **crypto:**  </br>A collection of scripts to demonstrate a wide variety of different techniques and algortihms used in modern cryptography.</br> -- <ins>decrypt_rsa_compare_speed.py:</ins></br>A script to show differences in speed when decrypting RSA with/without using the chinese rest theorem.</br> -- <ins>wieners_attack_on_rsa.py:</ins></br>A sample implementation of wieners attack on RSA for a small private part d. </br> -- <ins>babystep_giantstep.py:</ins></br>A sample implementation of the baby step -> giant step algorithm to compute discrete logarithms.