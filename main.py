import json, random
import string,webbrowser

with open("defualt.json") as defualt:
    defualtObj = json.load(defualt)
letters = string.ascii_lowercase
print("\nSupported Manga Site : manganelo.com\n")
while True:
  

  cmd = input("Select Commamd:")
  file_name = "list.json"
  if cmd == "add":
    nums_input = ''.join(random.choice(letters) for i in range(10))
      
    detail = input(f"Add Link :")
    a_dict = {f"t{nums_input}": detail}
    with open(file_name, "r+") as file:
        data = json.load(file)
        data.update(a_dict)
        file.seek(0)
        json.dump(data, file)
          
        print(" ~ Manga Added ~")
  if cmd =="read":
    with open(file_name, "r") as file_r:
      datar=json.load(file_r)

    for i in datar:
      print(f"{list(datar.keys()).index(i)+1}.{datar[i]}")
    chpA=int(input("Select Manga:"))-1
    chpB=input("Select Chapter:")
    copper=list(datar.values())[chpA]
    copperdex=copper.find("chapter_")
    copperA=copper[copperdex:]
    copperB=copperA.find("_")
    chpNumber=copperA[copperB+1:]
    maindex=copperdex+copperB+1
    deltachp=copper[:maindex]+chpB
    listkey=list(datar.keys())[chpA]
    print("Manga Opened In Your Browser")
    datar[listkey] = deltachp
    with open(file_name, "w") as file_rw:
      json.dump(datar, file_rw)
    webbrowser.open(deltachp)
    
  if cmd == "help":
      print(
          "add = Add New Manga\n\nclear = clear manga list\nshow = show all manga list"
      )
  if cmd == "show":
      with open(file_name, "r") as file_r:
          datar = json.load(file_r)
          print(datar)

  if cmd == "clear":
      with open(file_name, "w") as Clear:
          json.dump(defualtObj, Clear)
          print(" ~~ Manga Cleared ~~")
