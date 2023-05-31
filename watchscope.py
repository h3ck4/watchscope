import requests,os,json
from comparedata import compare

print("[*] Initializing the script, beginning to check if the data already exists...")

# Fetching the data from github repo, quiting the program if an error happens
try:
    response = requests.get("https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/hackerone.json", timeout=5)
except:
    print("[!] Failed to retrive the data!")
    quit()

# Checking if the file already exists.
if os.path.exists("hackerone.json"):
    print("[*] File already exist, beginning the comparison...")
    compare("hackerone.json",response.text)
    response.close()
else:
    print("[*] No data have been found, beginning to make a new one...")

    # Creating a new file with the response data within it.
    file = open("hackerone.json","w")
    file.write(response.text)
    file.close()
    print("[*] Succesfully retrive the data.")
    print("[#] Jobs done, Happy hacking :)")