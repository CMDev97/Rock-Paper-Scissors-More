import random
import constant


def read_file_to_dictionary():
    ratings = {}
    with open(constant.RATING_FILE, 'r') as file:
        for line in file:
            name, rating = line.split()
            ratings[name] = int(rating)
    return ratings


def save_new_ratings(ratings):
    with open(constant.RATING_FILE, 'w') as file:
        for user_name, rating in ratings.items():
            file.write(f"{user_name} {rating}\n")


def show_user_rating(user, ratings):
    rating = 0
    if user in ratings:
        rating = ratings[user]
    print(f"Your rating: {rating}")


def add_user_rating(user, ratings, result):
    if user not in ratings:
        ratings[user] = constant.RATING_VALUES[result]
    else:
        ratings[user] += constant.RATING_VALUES[result]


def read_user_info():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    return user_name


def get_relations(options, chosen):
    index = options.index(chosen)
    others = options[index + 1:] + options[:index]
    half = len(others) // 2
    defeats = others[half:]
    beaten_by = others[:half]
    return defeats, beaten_by


def evaluate_hand(options, user_command, computer_command):
    if user_command == computer_command:
        return constant.DRAW
    defeats, beaten_by = get_relations(options, user_command)
    if computer_command in defeats:
        return constant.WIN
    else:
        return constant.LOSS


def print_result_hand(result, computer_command):
    if result == constant.DRAW:
        print(f"There is a draw ({computer_command})")
    elif result == constant.LOSS:
        print(f"Sorry, but the computer chose {computer_command}")
    else:
        print(f"Well done. The computer chose {computer_command} and failed")


def get_user_command(validation):
    while True:
        user_command = input().lower()
        if user_command not in validation:
            print("Invalid input")
        else:
            return user_command


def input_game_options():
    while True:
        options_game = input()
        if not options_game or not options_game.strip():
            return constant.SIMPLE_GAMES

        values = (options_game.strip()
                  .replace(" ", "")
                  .lower().split(","))

        if len(values) >= 3:
            return values
        print("Invalid input")


def get_validation_command(games):
    validation = list(games)
    validation.extend(constant.OTHER_COMMAND)
    return validation


def game():
    continue_game = True
    ratings = read_file_to_dictionary()
    user_name = read_user_info()
    option_game = input_game_options()
    validation_input = get_validation_command(option_game)
    print("Okay, let's start")
    while continue_game:
        user_command = get_user_command(validation_input)
        if user_command == constant.EXIT:
            continue_game = False
            continue
        if user_command == constant.RATING:
            show_user_rating(user_name, ratings)
            continue
        computer_choice = random.choice(option_game)
        result = evaluate_hand(option_game, user_command, computer_choice)
        add_user_rating(user_name, ratings, result)
        print_result_hand(result, computer_choice)
    save_new_ratings(ratings)
    print("Bye!")


if __name__ == '__main__':
    game()
