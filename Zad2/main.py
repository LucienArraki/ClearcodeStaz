import SpellCalculator as sp

if __name__=="__main__":
    print("Testy")
    print(str(sp.damage("12343214")) + " - 12343214")
    print(str(sp.damage("Fe")) + " - Fe")
    print(str(sp.damage("feAi")) + " - feAi")
    print(str(sp.damage("aiai")) + " - aiai")
    print(str(sp.damage("fefefeai")) + " - fefefeai")
    print(str(sp.damage("feeai")) + " - feeai")
    print(str(sp.damage("feaineain")) + " - feaineain")
    print(str(sp.damage("jee")) + " - jee")
    print(str(sp.damage("()90123[]ASDfdafafeajain")) + " - ()90123[]ASDfdafafeajain")
    print(str(sp.damage("fexxxxxxxxxxai")) + " -  fexxxxxxxxxxai")
    print(str(sp.damage('xxxxxfejejeeaindaiyaiaixxxxxx')) + ' -  xxxxxfejejeeaindaiyaiaixxxxxx')