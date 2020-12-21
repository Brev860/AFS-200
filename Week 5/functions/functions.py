x=[99,23,5]
def findmax():
    return(max(x))

print(findmax())

message = input("Type word: ")

def countCaps():
    count = sum(1 for c in message if c.isupper())
    return(count)

print("Capital Letters: ", countCaps()) 