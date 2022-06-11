import os
import sys

# tratamento de erros = 2 estratégias
# 1) LBYL - Look Before you Leap

if os.path.exists("09_names.txt"):
    input("...") # Race Condition
    names = open("09_names.txt").readlines()
else:
    print("[Error] File 09_names.txt not found")

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the file")
    sys.exit(1)