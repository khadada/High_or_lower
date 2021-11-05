import random
def cpu_choices(ob):
    selects = []
    for _ in range (2):
        selects.append(random.choice(ob))
    return selects

def answer_checker(ob):
    high_follower_count = ob[0]["follower_count"]
    correct_compare = ""
    for person in ob:
        if person["follower_count"] > high_follower_count:
            high_follower_count = person["follower_count"]
            print(person["name"])
            correct_compare = 'b'
        else:
            correct_compare = 'a'
    return correct_compare



def print_compare(ob,a_b):
    select = 0
    if a_b.lower() == "a":
        select = 0
    elif a_b.lower() == "b":
        select = 1
    message = f"compare {a_b.upper()}: {ob[select]['name']}, {a_b.upper()} {ob[select]['description']}, {a_b.upper()} {ob[select]['country']} "
    print(message)


def restart ():
    print('You get the highest score for this game wait for next level for more tasks')
    print('Thank you!!')
    print("#" * 100)
    user_name = input("What's your name?  ")
    print(f"Congratulations {user_name}")
    name = user_name.split()[0]
    print(name, end=' ')
    again = input(".Do you need you need to play again? type [y] or [n] => ").lower()
    if again == "y":
        return True
    elif again == 'n':
        print('Thank you  to play my game')
        return False
    else:
        print(f"Sorry. {user_name} the '{again}' is invalid value. ")
        print('The game will close now!')
        return False
