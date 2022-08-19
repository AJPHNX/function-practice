def hello():
    print("Greeting")

def pack(a,b,c):
    list =[a,b,c]
    print(list)

food_list =["tacos","pizza","cheese in general"]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")



hello()
pack(1,5,4)
eat_lunch(food_list)