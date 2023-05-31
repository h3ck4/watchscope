import json
from structure import hackeroneData
# TODO : check the data in each program correctly tomorrow

def compare(file1,response):
    newData = json.loads(response)
    file = open(file1 , "r")
    rawdata = file.read()
    file.close()
    oldData = json.loads(rawdata)   
    newProgram = {}

    #loop through each program in new data
    index = 0
    for program in newData:
        if not program in oldData:  
            print(f"[*] Some changes have been found, beggining to check. ID={program['id']}")
            for data in program:
                if program[data] not in oldData[program][data]:
                    print(program[data])
                    newProgram.update(program[data])
        index += 1
    # if len(newProgram) == 0:
    #     print("[*] Succesfully compared the data, no new program have been found.")
    #     quit()
    # else:
    #     #print(newData[0]["relationships"]["structured_scopes"]["data"][0]["id"])
    #     jsonData = json.dumps(newProgram, indent=4)
    #     useful = open("hackeroneData", "w")
    #     useful.write(jsonData)
    #     useful.close()
    #     file = open(file1 ,"w")
    #     file.write(response)