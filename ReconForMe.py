import os
import sys
import shodan
import requests
import json


#===============FUNCTIONS===============

def callNuclei(target):   
    os.system("echo 'SCAN VULNERABILITIES OF YOUR TARGET: ' > ./report/vulns_result.txt")
    nuclei = "nuclei -u " + target + " -t ./templates/*.yaml -o ./report/vulns_result.txt"
    return nuclei

def callShodan(target):

    with open('./api.txt', 'r') as f:
      SHODAN_API_KEY = f.readline()

    api = shodan.Shodan(SHODAN_API_KEY)

    dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY

try:
  
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json() [target]
  
    host = json.dumps(api.host(hostIP), indent = 4, sort_keys = True)

   
    with open('./report/shodan_result.json', 'w') as f:
      
      if len(host) != 0:
                          
           f.write(host)

except:
    'An error occured'


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

def callWhois(target):
    os.system("echo 'WHO IS IS YOUR TARGET: ' > ./report/scan_result.txt")
    whois = "whois " + target + " >> ./report/whois_result.txt"
    return whois



#===============MAIN===============

if not os.path.isdir('./report'): os.system("mkdir ./report")
   

print("Hello Friend")
print("Who is your target?", end=" ")
target = input()



os.system(callWhois(target))
os.system(callNmap(target))
os.system(callSubfinder(target))
callShodan(target)
os.system(callNuclei(target))
print("Done! Check the report folder for your information")
print("Happy Hacking")










