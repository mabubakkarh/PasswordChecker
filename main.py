####### Dictionary Project- SummerII, London 2022 By Md Abubakkar ########
''' This is a program to check if passwords in a file are acceptable
    for given criteria such as number of length or number of Uppercase
    character allowed. To run this program simply type main.py and input all the
    criteria/conditions. passwordInput.txt file has all the passwords to check and
    Dictionery20K.txt has all the dictionary word that a password must avoid.
    After running the program, and inputting all the conditions, 
    passwordOutput.txt file will show what password was accepted and what was 
    not (including the information what condition was violated). For any question
    or comment please email me at abubakkar.howladar@gmail.com Thank you!!'''


"""
Orders of Password feature:
1. Length 
2. Alphabetic Characters 
 Upper Case
 Lower case
3. No dictionary words 
4. Not a given name 
5. Not a given email 
6. Numeric Characters (digits) 
7. Special Characters 
"""

# Invalid Reason 
reason = "(Valid)"

# Password criterias given from Userinput
passwordLengthInput = int(input("Condition 1: What is the min length of password?\n"))
# Uppercase letters length
upperCaseInput = int(input("Condition 2: What is the number of Capital letters you want?\n"))
# Uppercase letters length
lowerCaseInput = int(input("Condition 2: What is the number of Small letters you want?\n"))
# taking user name from the user
userNameInput = input("Condition 4: What is your name?\n")
# taking user email from the user
userEmailInput = input("Condition 5: What is your Email?\n")
# taking numaric characters from the user
numericCharactersInput = int(input("Condition 6: What is the number of numeric characters you want?\n"))
# taking special characters from the user
specialCharactersInput = int(input("Condition 7: What is the number of special characters you want?\n"))

# Counting how many upper and lower case characters
upperCount = 0
lowerCount = 0
numaricCount = 0
specialChCount = 0

# Special Characters
specialCharacters = '`~!@#$%^&*()_+-=[]{}|;:<>?,./'

#Opening the password from a given input file
passwordReader = open('passwordInput.txt', 'r')
fileData = passwordReader.read()
fileData = fileData.split() #Splitting all the strings

#Opening output file where we will write the passwords
passwordWriter = open('passwordOutput.txt', 'w')

dictionary = open('Dictionary20K.txt', 'r')
dictWords = dictionary.read()
dictWords = dictWords.split()
sortedWords = []
for word in dictWords:
  if len(word) >= 5:
    sortedWords.append(word)

# print(sortedWords)

# Iteratively checking if password's length is greater than or equal to the user defined length
for password in fileData:

  ##########CONDITION 1 CODE: LENGTH#############
  if len(password) >= passwordLengthInput:

    # iterating through password and checking how many uppercase and lowercase letters are there.
    for ch in password:
      if ch <= 'z' and ch >= 'a':
        lowerCount+=1
      if ch <= 'Z' and ch >= 'A':
        upperCount+=1
      # conting the numaric characters
      if ch <= '9' and ch >= '0':
        numaricCount+=1
      # Counting Special Characters
      if ch in specialCharacters:
        specialChCount +=1

    # Checking uppercase count and lowercase count with user input
    if upperCount >= upperCaseInput:
      if lowerCount >= lowerCaseInput:
        # for dictionary
        if password.lower() not in sortedWords:
          # checking user name with password
          if password != userNameInput:
            # checking email with password
            if password != userEmailInput:
              # checking numaric characters with user input
              if numaricCount >= numericCharactersInput:
                # checking special characters with user input
                if specialChCount >= specialCharactersInput:
                  reason = "(VALID)"
                else:
                  reason = "(INVALID for CON 7)"
              else:
                reason = "(INVALID for CON 6)"
            else:
              reason = "(INVALID for CON 5)" 
          else:
            reason = "(INVALID for CON 4)"
        else:
          reason = "(INVALID for CON 3 - Found In Dictionary)"
      else:
        reason = "(INVALID for CON 2 - Lower Case is not sufficient)"
    else:
      reason = "(INVALID for CON 2 - Upper Case is not sufficient)"

    # print(f"{password} - (VALID)")
    # passwordWriter.write(f"{password} - {reason}\n")

  # if the above condition not work then this block will execute
  else:
    reason = "(INVALID for CON 1)"
    # print(f"{password} - (INVALID for CON 1)")

    #Writing passwords in the output file
    # passwordWriter.write(f"{password} - (INVALID for CON 1)\n")
  
  # Reseting the default value
  upperCount = 0
  lowerCount = 0
  numaricCount = 0
  specialChCount = 0
  # print("What is happening?")
  # writing the file with result
  passwordWriter.write(f'{password} - {reason}\n')


# Closing the password writer file.
passwordWriter.close()
