import json
import random
with open("cards.json","r",encoding="utf8") as f:
    cards=json.load(f)

filteredCards=[]
filteredCardNames=[]
bannedSets=["spm","om1","spe","pspm","tle","tla","mar"]
for item in cards:
    if item["name"] not in filteredCardNames:
        try:
            if item["security_stamp"]=="triangle": #no ub
                #print("skipping UB")
                continue
                
        except:
            "I guess there's no stamp"
        try:
            if item["set"] in bannedSets: #no spiderman
                #print("skipping SPM")
                continue
        except:
            "???"
        filteredCards.append(item)
        filteredCardNames.append(item["name"])

with open("cardsFiltered.json","w",encoding="utf8") as f:
    f.write(json.dumps(filteredCards,indent=4))
