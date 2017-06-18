
def damage(text):
    if text.find('fe')<0:   #Start for 'fe'
        return 0

    text = findAndCut(text,'fe')
    dmg = [1]

    text = findAndCut(text[::-1],'ia')[::-1]    #End on 'ai'

    dmg.append(2)

    if text.find('fe')>=0:    #'fe' is only once
        return 0

    subspell = ['fe','je','jee','ain','dai','ne','ai','aine'],[1,2,3,3,5,2,2,4]     #Subspell damage

    i=0
    while i != len(text):
        maxIndex = -1
        for j in range(len(subspell[0])):
            if (text[i:len(subspell[0][j])+i]).find(subspell[0][j])==0:     #Search subspell
                if subspell[1][j] > maxIndex:
                    maxIndex=j                  #MaxIndex is index of best subspell damaga
        i+=1
        if maxIndex>=0:
            text = findAndCut(text,subspell[0][maxIndex])
            dmg.append(subspell[1][maxIndex])       #Add damage
            i=0
        else:
            dmg.append(-1)      #If no subspell

    spellDamage=0
    if(sum(dmg) <0):     #Damage
        spellDamage = 0
    else:
        spellDamage = sum(dmg)

    return spellDamage

def findAndCut(string,find):
    return string[string.find(find)+len(find):] #Cut string
