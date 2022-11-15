from roller import Roller


def main():
    rolling = True
    while rolling:
        try:
            dice_amount = int(input("how many dice do you want to roll at a time?"))
            roll_input = int(input("How many dice would you like to roll?"))
            dice_role = Roller(dice_amount=dice_amount)
            dice_role.roll(roll_input)
            dice_role.grab_rolls()
            rolling = False
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
