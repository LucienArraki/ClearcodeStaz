from collections import Counter

INDEX_YEAR=40       #Index of year in file
INDEX_MONTH=18      #Index of month in file
INDEX_SUCCESS=193   #Index of success in file

def group_by(*args,**kwargs):


    if(args.__len__()<2 or args.__len__()>2 or kwargs.__len__()>1):
        print("Dane bledne podac chciales padawanie")
        return {}
    success = None
    row = []
    if kwargs.__len__() > 0:
        success = list(kwargs.values())[0]


    'Table of year, month and success information'

    row = [[line[INDEX_YEAR:INDEX_YEAR+4],line[INDEX_MONTH:INDEX_MONTH+3],succes(line[INDEX_SUCCESS:INDEX_SUCCESS+1])]
           for line in args[0] if (line[INDEX_YEAR:INDEX_YEAR+4]).isdigit()]


    'Create dictionary'

    if(args[1]=='year' or args[1]=='month'):
        grouped={}
        if args[1] == 'year' and success == None:      #All year
            grouped=Counter([year[0] for year in row])
        elif args[1] == 'year' and success != None:     #Year with success
            grouped=Counter([year[0] for year in row if year[2]==success])
        elif args[1] == 'month' and success == None:    #All month
            grouped=Counter([month[1] for month in row if month[1] !="   "])
        elif args[1] == 'month' and success != None:     #Month with success
            grouped=Counter([month[1] for month in row if month[1] != "   " and month[2]==success])
    else:
        print("Dane bledne podac chciales padawanie")
        return {}


    'For print like in Example'

    print("{")
    endDictionary={}
    for i in range(grouped.__len__()):
        endDictionary[list(sorted(grouped.keys()))[i]] = list(grouped.values())[i]
        print("'" + str(list(endDictionary.keys())[i]) + "': " + str(list(endDictionary.values())[i]) + ",")
    print("}")
    return endDictionary


def succes(x):      #Change column Suc to bool
    if x == 'S':
        return True
    elif x == 'F':
        return False
    return ""
