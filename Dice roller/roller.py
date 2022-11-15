import random
import pandas
import matplotlib.pyplot as plt


class Roller:
    def __init__(self, dice_amount):
        self.n_side = 6
        self.dice_amount = dice_amount
        self.rolled_nums = []
        self.roll_count = 0

    def log_roll(self, total):
        df = pandas.DataFrame(total, columns=["Total"])
        df.to_csv("rolls.csv", index=False)

    def roll(self, rolls):
        roll = 0
        for _ in range(1, rolls):
            for _ in range(self.dice_amount):
                die1 = random.randint(1, self.n_side)
                roll = roll + die1
            self.rolled_nums.append(roll)
            roll = 0
            # self.roll_count += 1
            # print(self.roll_count)
            # print(f"{die1} + {die2} = {roll}")
        self.log_roll(self.rolled_nums)

    def grab_rolls(self):
        df = pandas.read_csv("rolls.csv")
        df_list = df.Total.values.tolist()
        x_values = None
        y_values = []
        max_range = (self.n_side * self.dice_amount) + 1
        for num in range(self.dice_amount, max_range):
            y_values.append(df_list.count(num))
        x_values = [num for num in range(self.dice_amount, max_range)]
        # print(f"{x_values}, {y_values}")
        plt.title("Dice Roller")
        plt.xlabel("Dice total")
        plt.ylabel("Frequency")
        plt.plot(x_values, y_values, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)
        plt.show()
