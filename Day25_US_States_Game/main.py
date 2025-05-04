import turtle
import pandas
from state_turtle import StateTurtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.screensize(725, 500)
screen.addshape(image)
#Use image as background for game screen:
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()


#If you need to get the location of places on the screen:
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

guessed_states = []

while len(guessed_states) < 50:

    #Dialog screen to ask for information; includes OK and Cancel buttons.
    #Keep track of correct guesses in title of dialog.
    if len(guessed_states) == 0:
        title = "Guess the State"
    else:
        title = f"{len(guessed_states)}/50 States Correct"

    answer_state = screen.textinput(title=title, prompt="What's another state name?")
    answer_state = answer_state.title().strip()

    if answer_state.lower() == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        # missing_states =[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed_states.csv")
        break

    # Check if the answer_state is in the DataFrame
    if answer_state in state_data.state.values and answer_state not in guessed_states:
        # Pull out and save the entire row matching entered answer_state. This will be saved as a Panda Series
        state_row = state_data[state_data.state == answer_state]
        # Use .item() if you just want the value for the columnname. Otherwise, it will also contain the line's index number and cause a data mis-match.
        state_name = state_row.state.item()
        x_loc = int(state_row.x.item())
        y_loc = int(state_row.y.item())
        print(f"State: {state_name}, ({x_loc}, {y_loc})") # Troubleshooting
        new_state = StateTurtle(state_name, x_loc, y_loc)
        guessed_states.append(answer_state)


# Similar to exitonclick()
turtle.mainloop()







