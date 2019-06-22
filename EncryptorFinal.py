import math
file_contents = []
f = open('passwords.txt','r')
for line in f:
    file_contents.append(line.strip())

new_path = '/Users/KohlStark/Documents/Python/Encryption Algorithms/Encrypted_Passwords.txt'
def scrambler(number):
  number = (((number * 103) / 6) + 7123)
  #number = number + 1
  return number

return_list = []
def encryptor(file_contents):
  print ("Passwords before encryption: ", file_contents)
  for i in file_contents:
      pass_list = []
      for letter in i:
        letter = ord(letter)
        #print (letter) # ASCII value of the letter in the password string
        pass_list.append(letter) # Append the int to a list
      #print (pass_list) # print the list 
      counter = 0 
      for items in pass_list:
        pass_list[counter] = int(scrambler(pass_list[counter]))
        #print ("HI", pass_list[counter]) #Number after manipulation
        pass_list[counter] = chr(pass_list[counter])
        #print (pass_list[counter]) #Number after being converted back to regular string
        counter += 1
        values = ''.join(str(v) for v in pass_list) # crunch the list into one string
      return_list.append(values)
      with open(new_path, 'w') as f:
          for item in return_list:
              f.write("%s\n" % item)
  print ("Passwords after encryption: ", return_list)
  return return_list

#user_pass = input("Enter a password to be encrypted: ")


encryptor(file_contents)
f.close()

import Decryptor

