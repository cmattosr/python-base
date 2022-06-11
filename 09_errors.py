import os
import sys

# tratamento de erros = 2 estratégias
# 1) LBYL - Look Before you Leap

# if os.path.exists("09_names.txt"):
#     input("...") # Race Condition
#     names = open("09_names.txt").readlines()
# else:
#     print("[Error] File 09_names.txt not found")

# if len(names) >= 3:
#     print(names[2])
# else:
#     print("[Error] Missing name in the list")
#     sys.exit(1)
    
    
# 2) EAFP - Easy to Ask for Forgiveness than Permission (essa é a solução preferida na maioria dos casos)

try:
    names = open("09_names.txt").readlines() # FileNotFoundError
    # 1 / 0 # ZeroDivisionError
    # print(names.banana) # AttributeError
# except: # bare except
except FileNotFoundError as e:
    #print("[Error] File 09_names.txt not found")
    print(f"[Error] {str(e)}")
    sys.exit(1)
except ZeroDivisionError as e:
    # print("[Error] You can´t divide by zero")
    print(f"[Error] {str(e)}")
    sys.exit(1)
except AttributeError:
    print("[Error]  'list' does not have 'banana'")
    sys.exit(1)
else:
    print("[Success]")
finally:
    print("[Executa sempre o finally, com sucesso ou erro]")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
    
# Criar seu proprio erro
try:
    raise RuntimeError("Ocorreu um erro")
    1 / 0
except Exception as e:
    print(f"[Error] {str(e)}")