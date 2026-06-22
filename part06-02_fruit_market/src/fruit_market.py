# write your solution here
def read_fruits():
    with open("fruits.csv") as fruits:

        pricebook = {}
        for line in fruits:
            line = line.replace("\n", "")
            fruit, price = line.split(";")
            pricebook[fruit] = float(price)
            print(line)
        return pricebook
