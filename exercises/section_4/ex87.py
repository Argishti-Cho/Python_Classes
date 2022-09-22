
def shippingRateCalculator(numberOfItems):
    firstItem = 10.95
    subsequentItem = 2.95
    if numberOfItems > 0 and numberOfItems == 1:
        subTotalRate = numberOfItems * firstItem
        return subTotalRate
    elif numberOfItems > 1:
        TotalRate = firstItem + subsequentItem * (numberOfItems-1)
        return TotalRate
    else:
        return 'somethong went wrong'

def main():
    userOrder = int(input('Enter your order quantity:  '))
    result = shippingRateCalculator(userOrder)
    return f'The cost of your order is ${round(result, 3)}'

if __name__ == "__main__":
    print(main())


