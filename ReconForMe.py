import os

print("Hello, Bryan.")
print("Who is your target? ", end=" ")

target = input()

os.system("mkdir ./report")
os.system("echo 'SCAN OF YOUR TARGET: ' > ./report/scan_result")

print("Agressive?", end=" ")
answer = input()
answer = answer.lower()
check = True

if answer == "no"  or answer == "n":
   nmap = "sudo nmap " + target + " >> ./report/scan_result"
   check = False 
 
if answer == "yes"  or answer == "y":
   nmap = "sudo nmap -v -A " + target + " >> ./report/scan_result"
   check = False

if check == True:    
    print("Please say yes or no, sir")

print(nmap)

os.system(nmap)
