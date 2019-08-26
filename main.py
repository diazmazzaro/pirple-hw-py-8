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

# Checks if user data derectory already exists
def checkUsrData ():
  path = ".usrdata"
  if not os.path.isdir(path):
    os.mkdir(path)

# Request user to enter file's number.
def reqLineNumber():
  line = ""
  while not line.isdigit():
    if line:
      print("\033[0;31;40mInvalid \033[1;31;number\033[0;37;40m ")
    line = input("Please enter a line number:")
  return line

# Request user to enter a note.
def reqNote(msg):
  note = ""
  f = True
  while not note:
    if not f:
      print("\033[0;31;40mEmpty \033[1;31;40mnote.\033[0;37;40m")
    else:
      f = False
    note = input(msg).strip()
  return note


# Checks if file already exists and prompt options
def chekFile (file):
  act = []
  if os.path.isfile(".usrdata/" + file):
    action = ""
    while action not in ['r', 'd', 'a', 'l']:
      if action:
        print("\033[0;31;40mInvalid \033[1;31;40moption\033[0;37;40m ")
      print("Please select an option:\n \033[1;33;40mr\033[0;37;40m - Read file\n \033[1;31;40md\033[0;37;40m - Delete the file and start over\n \033[1;36;40ma\033[0;37;40m - Append the file\n \033[1;32;40ml\033[0;37;40m - Replace a single line\n")
      action = input("Option:").lower()
      act.append(action)
      if action == 'l':
        line = reqLineNumber()
        act.append(line)
  else:
    act.append("w")
  return act

# Handle user's selected option
def handleOption (file, op):
  if op[0] == 'w':
    note = reqNote("You are creating a \033[1;36;40mnew File\033[0;37;40m. Please enter the note:\n")
    noteFile = open(".usrdata/" + file, "w")
    noteFile.write(note)
    noteFile.close()
  elif op[0] == 'd':
    note = reqNote("This file is now \033[1;31;40mempty\033[0;37;40m. Please enter a new note:\n")
    noteFile = open(".usrdata/" + file, "w")
    noteFile.write(note)
    noteFile.close()
  elif op[0] == 'a':
    note = reqNote("Please enter a new note:\n")
    noteFile = open(".usrdata/" + file, "a")
    noteFile.write("\n" + note)
    noteFile.close()
  elif op[0] == 'r':
    noteFile = open(".usrdata/" + file, "r")
    l = 0
    for line in noteFile:
      l+=1
      print("\033[1;33;40m[\033[0;35;40m"+ str(l) + "\033[1;33;40m]\033[0;37;40m " + line, end="")
    print()
    noteFile.close()
  elif op[0] == 'l':
    noteFile = open(".usrdata/" + file, "r+")
    lines = noteFile.readlines()
    ln = int(op[1]);
    while ln > len(lines):
      ln = int(reqLineNumber())
    note = reqNote("Please enter a new note:\n")
    lines.insert(ln-1, note)


file_name = reqFileName()
checkUsrData()
actions = chekFile(file_name)
handleOption(file_name, actions)