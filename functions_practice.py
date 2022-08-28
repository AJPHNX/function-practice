def hello():
    print("Greetings!...and stuff...")

def pack(a,b,c):
    list =[a,b,c]
    print(list)

food_list =["tacos","pizza","fruit loops","cheese in general","whatever", "something healthy like pepperoni or something"]

def eat_lunch(list):
    alt = ["Next I ","After That I","I could possibly"]
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            elif i == (len(list))-1:
                print(f"And THEN....I eat {list[i]}")
            
            else:
                if (i % 2):
                    x=0
                elif (i % 3):
                    x=2
                else: 
                    x=1
    
                print(f"{alt[x]} eat {list[i]}")
def inner_fun(a,b):
    func_a= a+b
    func_b= a%b
    return func_a + func_b

def lunch_lady(name,lunch="Mystery Meat"):
    return f"{name}likes to eat {lunch} for lunch"

def sum_n_product(num1,num2):
    return f"the sum is {num1+num2} the product is {num1+num2}"
    
# alias_arb_args = arb_args

def arb_mean(*numbers):
    sum = 0

    for number in numbers:
        sum += number
    
    return sum / len(numbers)

def arb_longest_string(*strings):
	longest = ""
	for i in strings:
		if len(i) > len(longest):
			longest = i

	return longest
    
print("Hello:")
hello()
print("Pack:")
pack(1,5,4)
print("Eat Lunch:")
eat_lunch(food_list)
inner_fun(2,5)