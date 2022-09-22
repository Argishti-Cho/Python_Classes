import math

def taxiFare(basefare=4.00, cost=0.25, everyTravel=1):
    total = basefare + cost*everyTravel
    return total

def main():
    a = float(input('Enter the basefare according to your region:  '))
    b = float(input('Enter the cost per every 140 meters according to your region:  '))
    c = float(input('How many kilometers you ride:  '))
    result = taxiFare(a, b, c)
    return f'the cost of your ride is: {result}'

if __name__ == "__main__":
    print(main())


