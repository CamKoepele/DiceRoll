##diceroll.py
#koepele
#4/2020
#create a program that rolls two di and stores the totals in a dic


#create func to roll to dice and find sum
def roll():
    import random
    total = random.randint(1,6) + random.randint(1,6)
    return total


def main():
    total = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    expected_outcome = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67,
                        8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}
    #roll 1k ***This section of code was advised by Ira Griffin
    for i in range(1000):
        outcome = roll()
        total[outcome] += 1

    #calculate %
    for i in range(2, 13):
        total[i] = total[i]/10
        print("Total:{} \tPercentage:{}  Expected Percentage:{}"
              .format(i, total[i], expected_outcome[i]))

main()
