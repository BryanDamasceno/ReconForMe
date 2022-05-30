import os

#===============FUNCTIONS===============
def callSubfinder(target):
   os.system("echo 'SUBDOMAINS OF YOUR TARGET: ' > ./report/enumeration_result.txt")
   subfinder = "subfinder -d " + target + " >> ./report/enumeration_result.txt" 
   return subfinder

def callNmap(target):
   os.system("echo 'SCAN OF YOUR TARGET: ' > ./report/scan_result.txt")

   print("Agressive?", end=" ")
   answer = input() 
   answer = answer.lower()
   check = True

   if answer == "no"  or answer == "n":
      check = False
      nmap = "sudo nmap " + target + " >> ./report/scan_result.txt" 
      return nmap
   
   if answer == "yes"  or answer == "y":
      check = False
      nmap = "sudo nmap -v -A " + target + " >> ./report/scan_result.txt"
      return nmap

   if check == True:    
      print("Please say yes or no, sir")
      callNmap(target)


if not os.path.isdir('./report'): os.system("mkdir ./report")
   

print("Hello, Bryan.")
print("Who is your target?", end=" ")
target = input()






os.system(callNmap(target))
os.system(callSubfinder(target))
print("Scanning...")
