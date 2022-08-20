def hello():
    print("Greetings!...and stuff...")

def pack(a,b,c):
    list =[a,b,c]
    print(list)

food_list =["tacos","pizza","fruit loops","cheese in general","hmmmm..."]

def eat_lunch(list):
    alt = ["Next","After That","I could possibly"]
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            elif i == (len(list))-1:
                print(f"And THEN....I eat {list[i]}")
            
            else:
                if (i % 2) == 0:
                    x=0
                elif (i % 3) == 0:
                    x=2
                else: 
                    x=1
                print(f"{alt[x]} I eat {list[i]}")


print("Hello:")
hello()
print("Pack:")
pack(1,5,4)
print("Eat Lunch:")
eat_lunch(food_list)