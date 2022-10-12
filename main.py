import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATE GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_states = data.state.to_list()

guessed_list = []

while len(guessed_list) < 50:

    answer_state = screen.textinput(title=f"Score: {len(guessed_list)}/50",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        missed_states = [states for states in list_states if states not in guessed_list]
        missed = pandas.DataFrame(missed_states)
        missed.to_csv("states_to_learn.csv")
        break
    if answer_state in list_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinate = data[data.state == answer_state]
        t.goto(int(coordinate.x), int(coordinate.y))
        t.pendown()
        t.write(answer_state)



