# The file for collecting user's input
"""
Collect:
    Name
    Amount paid
        - who is spliitng this?
"""
# Data structure like this:
# jon: ( [100, [a,b,c]], [200, [b]], [50, [c]] )
# jon paid total of 3 bills


def CollectInput():
    name = ""
    amount = 0.0
    paid_person = []



    # Check if the name already exist
    # if yes, add the data under the same person
    name = input("Enter your name: \n")
    #print(name)


    amount = float(input("Enter bill amount: \n"))
    #print(f"{name} paid {amount}")

    while True:
        person = input("who also paid? Enter 'DONE' when finish entering the list \n")
        if person == "DONE":
            break
        else:
            paid_person.append(person)
    #print(paid_person)

    print(f"{name} paid {amount} with {paid_person}")


    


