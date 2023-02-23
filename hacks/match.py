from tkinter import *
from random import *
from threading import *
from time import sleep

real_database = []

root = Tk()
root.title("Match Game")
root.geometry("750x450")

good = ["Apple", "Almond", "Avocado", "Banana", "Bean", "Blueberry",
        "Broccoli", "Brussels-Sprouts", "Carrots", "Celery", "Chicken-Breast", "Cucumber",
        "Eggs", "Kiwi", "Lettuce", "Milk", "Mushroom", "Orange",
        "Spinach", "Strawberry", "Salmon", "Tomato", "Walnut", "Whole-Grain-Bread"]
bad = ["Bacon", "Chip", "Chicken-Nugget", "Donut", "Fries", "Hamburger",
       "Hot-Dog", "Ice-Cream", "Pizza", "Popcorn", "Soda", "White-Bread"]
shuffle(good)
shuffle(bad)
foods = 2 * (good[:12] + bad[:6])
shuffle(foods)

start_frame = Frame(root)
start_frame.pack()
game_frame = Frame(root)
end_frame = Frame(root)


class Tile(Button):
    def __init__(self):
        Button.__init__(self, game_frame, text="", font=("Arial", 15), width=10, height=2, command=self.onclick)
        self.matched = False

    def onclick(self):
        if not self.matched:
            global current, timePassed, matches, state
            self.config(text=linked[self].replace("-", "\n"))
            if current is None:
                current = self
            elif linked[current] == linked[self]:
                if current != self:
                    self.matched = True
                    current.matched = True
                    self.config(fg="gray")
                    current.config(fg="gray")
                    if bad.count(linked[self]):
                        timePassed += 10
                    else:
                        matches += 1
                        if matches == 1:
                            state = 2
                            end_frame.pack()
                            game_frame.forget()
                            ending()
                    current = None
            else:
                current.config(text="")
                current = self


def startGame():
    game_frame.pack()
    start_frame.forget()


buttons = [Tile() for i in range(36)]
linked = {}
current = None
matches = 0
state = 1
title = Label(start_frame, text="Health Match", font=("Arial", 54))
title.grid(row=0, column=0)
start_button = Button(start_frame, text="Start", font=("Arial", 24), command=startGame)
start_button.grid(row=1, column=0, pady=50)

timer = Label(game_frame, text='Time: 0', font=('Arial', 18))
timer.grid(row=0, column=4, columnspan=3, sticky=E)
timePassed = -0.01


def timing():
    global timePassed, state
    while state != 2:
        if state == 1:
            timePassed += 0.01
            timer.config(text="Time: {0:.2f}".format(timePassed))
        sleep(0.01)


def binaryInsert(value, aList):
    low = 0
    high = len(aList) - 1
    while low < high:
        mid = (low + high) // 2
        if value[1] < aList[mid][1]:
            high = mid
        else:
            low = mid + 1
    return aList[:low] + [value] + aList[low:], low


def ending():
    global timePassed
    final_time.config(text="Your Time: {0:.2f}".format(timePassed))
    final_time.grid(row=0, column=0, columnspan=5, pady=20)
    nameEntry.grid(row=1, column=0)
    nameButton.grid(row=2, column=0)


def cont():
    global real_database, username
    nameEntry.grid_forget()
    nameButton.grid_forget()
    rank_label = Label(end_frame, text="Rank", font=("Arial", 18))
    rank_label.grid(row=1, column=0)
    div1 = Label(end_frame, text="|", font=("Arial", 18))
    div1.grid(row=1, column=1)
    name_label = Label(end_frame, text="Name", font=("Arial", 18))
    name_label.grid(row=1, column=2)
    div2 = Label(end_frame, text="|", font=("Arial", 18))
    div2.grid(row=1, column=3)
    time_label = Label(end_frame, text="Time", font=("Arial", 18))
    time_label.grid(row=1, column=4)
    bar1 = Label(end_frame, text="--------", font=("Arial", 18))
    bar1.grid(row=2, column=0)
    div3 = Label(end_frame, text="|", font=("Arial", 18))
    div3.grid(row=2, column=1)
    bar2 = Label(end_frame, text="--------", font=("Arial", 18))
    bar2.grid(row=2, column=2)
    div4 = Label(end_frame, text="|", font=("Arial", 18))
    div4.grid(row=2, column=3)
    bar3 = Label(end_frame, text="--------", font=("Arial", 18))
    bar3.grid(row=2, column=4)
    real_database, finalRank = binaryInsert([username.get(), timePassed], real_database)
    for i in range(5):
        if len(real_database) > i:
            score = [Label(end_frame, text=str(i + 1), font=("Arial", 18)),
                     Label(end_frame, text="|", font=("Arial", 18)),
                     Label(end_frame, text=real_database[i][0], font=("Arial", 18)),
                     Label(end_frame, text="|", font=("Arial", 18)),
                     Label(end_frame, text="{0:.2f}".format(real_database[i][1]), font=("Arial", 18))]
            for j in range(5):
                score[j].grid(row=3 + i, column=j)
    if finalRank > 5:
        score = [Label(end_frame, text="........", font=("Arial", 18)),
                 Label(end_frame, text="|", font=("Arial", 18)),
                 Label(end_frame, text="........", font=("Arial", 18)),
                 Label(end_frame, text="|", font=("Arial", 18)),
                 Label(end_frame, text="........", font=("Arial", 18))]
        for j in range(5):
            score[j].grid(row=8, column=j)
        score = [Label(end_frame, text=str(finalRank + 1), font=("Arial", 18)),
                 Label(end_frame, text="|", font=("Arial", 18)),
                 Label(end_frame, text=real_database[finalRank][0], font=("Arial", 18)),
                 Label(end_frame, text="|", font=("Arial", 18)),
                 Label(end_frame, text="{0:.2f}".format(real_database[finalRank][1]), font=("Arial", 18))]
        for j in range(5):
            score[j].grid(row=9, column=j)



username = StringVar()
final_time = Label(end_frame, text="Your Time: {0:.2f}".format(timePassed), font=("Arial", 24))
nameEntry = Entry(end_frame, textvariable=username, font=("Arial", 16))
nameButton = Button(end_frame, text="Continue", font=("Arial", 16), command=cont)

for i in range(36):
    button = buttons[i]
    linked[button] = foods[i]
    button.grid(row=i // 6 + 1, column=i % 6)

t = Thread(target=timing)
t.start()
root.mainloop()
