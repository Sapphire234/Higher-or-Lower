import art
import os
import game_data
import random

# x=game_data.data[0]
# print(x['country'])
# print(LIST_LENGTH)

LIST_LENGTH=len(game_data.data)

def choose_items():
    indexes=[0,0]
    i1=random.randint(0, LIST_LENGTH-1)
    i2=random.randint(0, LIST_LENGTH-1)
    while i2==i1:
        i2=random.randint(0, LIST_LENGTH-1)
    indexes[0]=i1
    indexes[1]=i2
    return indexes
    
def who_higher(f1, f2):
    if f1>f2:
        return 1
    elif f1<f2:
        return 2
    else:
        return 0


score=0

def round():
    os.system("clear")
    print(art.logo)
    if score==0:
        print("\nWelcome to Higher or Lower!\n")
        print('—————————————————————————————————')
        
    else:
        print(f"\n| Score: {score} |\n")
        print('—————————————————————————————————')
        
    index_list=choose_items()
    
    pers1=game_data.data[index_list[0]]
    pers2=game_data.data[index_list[1]]
    
    name1=pers1["name"]
    name2=pers2["name"]
    description1=pers1["description"]
    description2=pers2["description"]
    country1=pers1["country"]
    country2=pers2["country"]
    no_followers1=pers1["follower_count"]
    no_followers2=pers2["follower_count"]
    print
    print(f"1) {name1} - {description1} ({country1})")
    print(art.vs)
    print(f"2) {name2} - {description2} ({country2})")
    print('—————————————————————————————————')
    print('')
    
    choice=int(input(f"\nType '1' if you think {name1} has more followers than {name2}, or '2' otherwise: "))
    
    while choice!=1 and choice!=2:
        print("\nInvalid input.")
        choice=int(input(f"Type '1' if you think {name1} has more followers than {name2}, or '2' otherwise: "))
    highest=who_higher(no_followers1, no_followers2)
    
    if highest==0 or highest==choice:
        return 1
    else:
        print(f"\nWrong! {name1} has {no_followers1}M followers and {name2} has {no_followers2}M followers")
        return 0
        
point=round()
score+=point
while point>0:
    point=round()
    score+=point
    
os.system("clear")
print(art.logo)
print(f"\n——————————————————————")
print(f"\n Your final score: {score}")
print(f"\n——————————————————————")

