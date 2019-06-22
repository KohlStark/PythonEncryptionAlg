import math
file_contents = []
f = open('Encrypted_Passwords.txt','r')
for line in f:
    file_contents.append(line.strip())

new_path = '/Users/KohlStark/Documents/Python/Encryption Algorithms/Decrypted_Passwords.txt'
def unscrambler(number):
  number = math.ceil((((number - 7123) * 6) / 103))
  #number = number - 1
  return number

restored_passwords = []
def decryptor(return_list):
  print ("Encrypted password: ", return_list)
  for i in return_list:
      pass_list = []
      for letter in i:
        letter = ord(letter)
        #print ("AS" ,letter) # ASCII value of the letter in the password string
        pass_list.append(letter)
      count = 0
      for items in pass_list:
        pass_list[count] = int(unscrambler(pass_list[count]))
        #print (pass_list[count]) #Number after manipulation
        pass_list[count] = chr(pass_list[count])
        count += 1
        values = ''.join(str(v) for v in pass_list) # crunch the list into one string
      restored_passwords.append(values)
      with open(new_path, 'w') as f:
          for item in restored_passwords:
              f.write("%s\n" % item)
  print ("Decrypted password: ", restored_passwords)
  return restored_passwords


decryptor(file_contents)
f.close()

