def items_input():
    while True:
        try :
            num = int(input("Enter the number of items : "))
            info_list = []

            for i in range(num):
                name = input("Enter the name of the item : ")
                weight = int(input("Enter the total weight of the item : "))
                value = int(input("Enter the total value of the item : "))
                item = [name,weight,value,value/weight]
                info_list.append(item)
            break
        except ValueError:
            print("Number of items, weight and value should be an integer!")

    info_list.sort(key=lambda item: item[3], reverse=True)
    return info_list

def cap():
    while True:
        try:
            capacity = int(input("Enter the maximum capacity of the knapsack : "))
            break
        except ValueError:
            print("Capacity should be an integer!")
    return capacity

def display(info_list,capacity):
    print("\n")
    print("Display".center(50,"-"))
    total_value = 0
    for name,weight,value,ratio in info_list:
        if capacity >= weight:
            total_value += value
            capacity -= weight
            print(f"Item Added : {name}\tValue Added : {value}")
        else:
            temp = round(capacity*ratio, 2)
            total_value += temp
            capacity = 0
            print(f"Item Added : {name}\tValue Added : {temp}")
            break
    print(f"Total Value : {total_value}")

items = items_input()
display(items,cap())
while True:
    print("""
    1. Enter 1 to Change Capacity and Calculate Again
    2. Enter 2 to Change Items and Calculate Again
    3. Enter 3 to Exit""")
    choice = input("Enter your choice : ")
    if choice == '1':
        display(items,cap())
    elif choice == '2':
        items = items_input()
        display(items,cap())
    elif choice == '3':
        break
    else:
        print("Invalid Choice!")