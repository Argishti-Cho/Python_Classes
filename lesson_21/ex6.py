def bus(bus_list):
    age = 16
    for i in bus_list:
        if i <= age:
            return 'too young'
        else:
            return 'Get Ready'
print(bus([52, 85, 17]))
        