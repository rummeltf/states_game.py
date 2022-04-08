import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("US States")
image_of_us = r"100_days\day_25\us-states-game-start\blank_states_img.gif"
screen.addshape(image_of_us)

turtle.shape(image_of_us)

def get_mouse_click_coor(x, y):
    print(x, y)

correct_answers = []
num_correct = len(correct_answers)

game_on = True
data = pandas.read_csv(r"100_days\day_25\us-states-game-start\50_states.csv")

while num_correct < 50:
    state_list = data["state"].to_list()
    user_guess = screen.textinput(title=f"{num_correct}/50 correct", prompt="Enter a state: ").title()
    # if user_guess == state name, append user_guess to correct_answers if not already in the list
    if user_guess in state_list:
        if user_guess not in correct_answers:
            correct_answers.append(user_guess)
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_data = data[data.state == user_guess]
            state_name.goto(int(state_data.x), int(state_data.y))
            state_name.write(user_guess)
            continue
    elif user_guess.lower() == "end":
        break
    elif user_guess not in state_list:
        print("Not a valid answer.")
        continue
    print(len(correct_answers))
if num_correct = 50:
    print("You win!")


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# convert the guess to title case [x]
# check if the guess is among the 50 states [x]
# write correct guess on map []
# use a loop to allow the user to keep guessing [x]
# record the correct guesses in a list [x]
# keep track of the score [x]