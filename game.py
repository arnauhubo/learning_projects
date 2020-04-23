# Write your code here
import random
import sys


def lose(opt):
    return "Sorry, but computer chose {}".format(opt)

def win(opt):
    return "Well done. Computer chose {} and failed".format(opt)

def draw(opt):
    return "There is a draw ({})".format(opt)

def play(opt_p, compt_opt, rules):
    #opcs = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air",
                  #"water", "dragon", "devil", "lightning", "gun"]
    person = rules.index(opt_p)
    new_list = rules[person + 1:len(rules)]
    new_list.extend(rules[0:person])
    result = "lose"
    if opt_p != compt_opt:
        machine = new_list.index(compt_opt)
    if opt_p == compt_opt:
        print(draw(compt_opt))
        result = "draw"
    elif machine < len(rules) // 2:
        print(lose(compt_opt))
    else:
        print(win(compt_opt))
        result = "win"

    return result

def get_name():
    print("Enter your name: ", end="")
    name = input()
    print("Hello,", name)
    return name

def get_score(name):
    ratings = open('rating.txt', 'r')
    score = 0
    for l in ratings.readlines():
        if name in l:
            score = l.split()
            score = score[1]
            score = int(score.replace("\n", ""))
    ratings.close()
    return score

def get_rules():
    opcs = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air",
            "water", "dragon", "devil", "lightning", "gun"]
    rules = input().lower().split(",")
    if rules[0] == "":
            return [opcs[0], opcs[8], opcs[2]]
    elif "exit" in rules[0]:
        print("Bye!")
        sys.exit()
    rules = list(rules)
    return rules

class Player:
    def __init__(self, n, s):
        self.name = n
        self.score = s

    def update_sc(self, res):
        if "win" in res:
            self.score += 100
        elif "draw" in res:
            self.score += 50

# -------------------- MAIN --------------------------------------------------------------------------------------------
name = get_name()
score = get_score(name)
my_player = Player(name, score)
rules = get_rules()
print("Okay, let's start")
while True:
    opt_p = input().lower()
    if "exit" in opt_p:
        print("Bye!")
        break
    elif "rating" in opt_p:
        print("Your rating:", my_player.score)
    elif opt_p not in rules:
        print("Invalid input")
    else:
        seed = random.randint(1, 1000000)
        random.seed(seed)
        compt_opt = random.choice(rules)
        res = play(opt_p, compt_opt, rules)
        my_player.update_sc(res)
# ----------------------------------------------------------------------------------------------------------------------
