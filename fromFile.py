import json
import random
with open("cardsFiltered.json","r",encoding="utf8") as f:
    cards=json.load(f)

#for item in cards:
#    print(item["name"])

count=50
current=0
goodcardlist=[]
bannedSets=["spm","om1","spe","pspm","tle","tla","mar"]
while current<count and len(cards)>0:
    targetCardIndex=random.randrange(0,len(cards))
    goodCard=True
    if cards[targetCardIndex]["legalities"]["vintage"]=="not_legal":
        goodCard=False
    if cards[targetCardIndex]["legalities"]["vintage"]=="banned":
        goodCard=False
    if cards[targetCardIndex]["name"] in goodcardlist:
        goodCard=False
    
    try:
        if cards[targetCardIndex]["security_stamp"]=="triangle": #no ub
            goodCard=False
    except:
        "I guess there's no stamp"

    #print(cards[targetCardIndex]["name"])
    #print(cards[targetCardIndex]["set"])
    if cards[targetCardIndex]["set"] in bannedSets: #no spiderman
        goodCard=False
    if goodCard:
        goodcardlist.append(cards[targetCardIndex]["name"])
        current+=1
    n=cards.pop(targetCardIndex)
    #print("removing"+str(n["name"]))


for item in sorted(goodcardlist):
    print(item)