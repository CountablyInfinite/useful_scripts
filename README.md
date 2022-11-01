
# useful_scripts
A wild collection of useful and (mostly) hacky scripts i wrote to get different kinds of work done. Be sure you understand what you are executing before you run any of them.

## Python

### resize_images.py
Python script to resize all images inside the current folder to 1/2 of the original size and export it to ./resized as .jpg in 80% quality.The binary has been built with pyinstaller to run on 64-Bit Windows systems.</br>```pyinstaller --onefile --icon=youricon.ico pythonfile.py```

### crypto
A collection of scripts to demonstrate a wide variety of different techniques and algortihms used in modern cryptography.

#### decrypt_rsa_compare_speed.py
A script to show differences in speed when decrypting RSA with/without using the chinese rest theorem.

#### wieners_attack_on_rsa.py
A sample implementation of wieners attack on RSA for a small private part d. 

#### babystep_giantstep.py
A sample implementation of the baby step -> giant step algorithm to compute discrete logarithms.

## Javascript

### kill_onevent.js
A short script that removes all "on" events that are actively blocking copying and pasting into a form. The script is heavily based on the solution of user Triynko in [this](https://stackoverflow.com/questions/4760132/improving-login-security-through-denial-of-copy-paste) stackoverflow discussion. Copy and Paste it into your browser console and enjoy. If you want to remove more events you can extent the array onevents with additional events.