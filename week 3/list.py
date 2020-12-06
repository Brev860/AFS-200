list = [1,2,3,4,5,24,35,46,33,75,48]

def lessThan(list):
    a = 5
    if (list < 5):
        return(True)
    else:
        return(False)    

filterlist = filter(lessThan, list )


for element in filterlist:
    print(element)