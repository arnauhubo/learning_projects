def check_coffee (w, m, g):
    if my_machine.water < w:
        print("Sorry, not enough water!")
        return False
    elif my_machine.milk < m:
        print("Sorry, not enough milk!")
        return False
    elif my_machine.coff_beans < g:
        print("Sorry, not enough coffee!")
        return False
    elif my_machine.dis_cups < 1:
        print("Sorry, not enough cups!")
        return False
    else:
        print("I have enough resources, making you a coffee!\n")
        return True

def buy_coffee ():
    print("What do you want to buy? 1 - espresso, "
          "2 - latte, 3 - cappuccino, back - to main menu:")
    opt = input()
    if opt != "back":
        opt = abs(int(opt))
        if opt == 1:
            if check_coffee(250, 0, 16):
                my_machine.action(-250, 0, -16, -1, 4)
        elif opt == 2:
            if check_coffee(350, 75, 20):
                my_machine.action(-350, -75, -20, -1, 7)
        else:
            if check_coffee(200, 100, 12):
                my_machine.action(-200, -100, -12, -1, 6)

def fill_machine ():
    print("Write how many ml of water do you want to add:")
    w = abs(int(input()))
    print("Write how many ml of milk do you want to add:")
    m = abs(int(input()))
    print("Write how many grams of beans do you want to add:")
    b = abs(int(input()))
    print("Write how many disposable cups of coffee do you want to add:")
    d = abs(int(input()))
    my_machine.action(w, m, b, d, 0)

def take_money ():
    print("I gave you $" + str(my_machine.cash))
    my_machine.action(0, 0, 0, 0, -my_machine.cash)


class coffee_machine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coff_beans = 120
        self.dis_cups = 9
        self.cash = 550

    def action(self, w, m, b, d, c):
        self.water += w
        self.milk += m
        self.coff_beans += b
        self.dis_cups += d
        self.cash += c

    def __repr__(self):
        return "The coffee machine has:\n" \
               "{0} of water\n" \
               "{1} of milk\n" \
               "{2} of coffee beans\n" \
               "{3} of disposable cups\n" \
               "{4} of money\n".format(self.water, self.milk, self.coff_beans, self.dis_cups, self.cash)

    def interaction(self, action):
        if action == "buy":
            buy_coffee()

        elif action == "fill":
            fill_machine()

        elif action == "take":
           take_money()

        elif action == "remaining":
            print(my_machine)


# START of main ------------------------
my_machine = coffee_machine()

inside = True
while inside:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    my_machine.interaction(action)
    if action == "exit":
        inside = False
# END of main --------------------------
















