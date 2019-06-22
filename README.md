# PythonEncryptionAlg
My first python3 project in an attempt to create my own encryption algorithm

This project is quite simple. By simply having the EncryptorFinal.py, Decryptor.py, and the passwords.txt files, all you need to do is run the EncryptorFinal.py. This will read the passwords.txt file, so you may place any kind of passwords you like in that file, encrypt them, and put them in an Encrypted_Passwords.txt file. 

The encryption algorithm to scramble the passwords is not very complex and prior to me finishing this project I did not know that most encryption algorithms created on your own are very easy to break. However, I still found enjoyment at having a crack at it. I simple translated the string to an integer value and did some extreme math to it and returned it back to string form. 

Once the files are encrypted inside of Encrypted_Passwords.txt, the EncryptorFinal.py calls the Decryptor.py which begins to read the encrypted passwords from the Encrypted_Passwords.txt file. It converts the string to an integer value and reverses the math since I know the encryption algorithm. Once the math is complete the integer value is again returned to string form and the restored passwords are placed in a new file named Decrypted_Passwords.txt. 

I had a lot of fun with this project, and learned alot from it since it was my first project in Python. This was mainly done in prepration for what I thought my Cyber Security course would go like that had no relivance I later learned. However, it did give me the python skills to help me through later projects! 

Try it out! Hope you enjoy!

