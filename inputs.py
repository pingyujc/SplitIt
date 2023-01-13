# The file for collecting user's input
"""
Collect:
    Name
    Amount paid
        - who is spliitng this?
"""
# Data structure like this:
# [ 
# [jon, [100, [a,b,c]], [200, [b]], [50, [c]] ], 
# [jc, [20, [a]]] 
# ]
# jon paid total of 3 bills


def CollectInput():
    name = ""
    bill_ppl = []
    amount = 0.0
    paid_person = []



    # Check if the name already exist
    # if yes, add the data under the same person
    name = input("Enter your name: \n")
    #print(name)


    amount = float(input("Enter bill amount: \n"))
    bill_ppl.append(amount)
    #print(f"{name} paid {amount}")

    while True:
        person = input("who also paid? Enter 'DONE' when finish entering the list \n")
        if person == "DONE":
            break
        else:
            paid_person.append(person)
    #print(paid_person)
    bill_ppl.append(paid_person)

    #print(f"{name} paid {amount} with {paid_person}")
    #print(f"{name} and {bill_ppl}")
    return name, bill_ppl


def ifExist(database, name):
    for i in range(len(database)):
        if name == database[i][0]:
            return True
    return False

def findIndex(database, name):
    for i in range(len(database)):
        if name == database[i][0]:
            return i
    return -1



def AddInput(database, name, bill_ppl):
    # this function will take 3 parameter:
    # a name and a list containing a single bill and ppl spliiting it, and the table it is adding to
    if ifExist(database=database, name=name) == False:
        temp = [name, bill_ppl]
        database.append(temp)
    else:
        database[findIndex(database=database, name=name)].append(bill_ppl)
        



    


