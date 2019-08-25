#  __    __  ____    __    ____       ___   
# |  |  |  | \   \  /  \  /   /      / _ \  
# |  |__|  |  \   \/    \/   / _____| (_) | 
# |   __   |   \            / |______> _ <  
# |  |  |  |    \    /\    /        | (_) | 
# |__|  |__|     \__/  \__/          \___/  
#                                           

# Dependencies
import os

# Request user to enter File name.
def reqFileName ():
  name = input("Please enter \033[1;32;40mFile\033[0;37;40m name: ").lower()
  if len(name) > 4 and '.txt' in name:
    return name
  else:
    print("\033[0;31;40mInvalid \033[1;31;40mFile name.\033[0;37;40m ")
    return reqFileName()

# 
def checkUsrData ():
  path = ".usrdata"
  if not os.path.isdir(path):
    os.mkdir(path)

# Checks if file already exists and prompt options
def chekFile (file):
  if os.path.isfile(".usrdata/" + path):
    action = input("Please enter \033[1;32;40mFile\033[0;37;40m name: ").lower()
  else:
    name = input("You are creating a \033[1;36;40mnew File\033[0;37;40m.Please enter  name: ").lower()

  return

file_name = reqFileName()
checkUsrData()