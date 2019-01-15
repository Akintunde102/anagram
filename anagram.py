s = 'slbe'
import itertools
with open('dict.json') as in_file:
    enDictJson = in_file.read()
    
import json
enDict = json.loads(enDictJson)

for x in range(2,len(s)+1):
    for perm in set(itertools.permutations(s,x)):
        joinedWords = "".join(perm)
        if joinedWords in enDict:
            print (joinedWords)