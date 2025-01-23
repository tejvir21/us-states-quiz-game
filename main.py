import turtle
import pandas

screen = turtle.Screen()

screen.title('U.S. States Game')

image = "blank_states_img.gif"

turtle.penup()

turtle.speed('fastest')

screen.addshape(image)

turtle.shape(image)

jimmy = turtle.Turtle()
jimmy.hideturtle()
jimmy.penup()
jimmy.speed('fastest')
jimmy.pencolor('black')

states_name_left = {}

states_data = pandas.read_csv('50_states.csv')

state_names = states_data.state.to_list()

states_name_left_list = state_names

already_guessed = []

def us_quiz():

    user_choice = screen.textinput(title=f"Guess the State  [{len(already_guessed)}/50]", prompt="What's another state's name?")

    if user_choice.title() in state_names and user_choice.title() not in already_guessed:
        already_guessed.append(user_choice.title())
        state_data = states_data[states_data.state == user_choice.title()]
        states_name_left_list.remove(user_choice.title())

        jimmy.goto(x=int(state_data.x),y=int(state_data.y))
        jimmy.write(arg=f"{user_choice.title()}",align='center',font=('Arial',8,'normal'))

    return True if user_choice.title() == 'Exit' else False
while len(already_guessed) < 50:
    rerun = us_quiz()

    if rerun:
        break

states_name_left['States'] = states_name_left_list

states_name_left_data = pandas.DataFrame(states_name_left)

states_name_left_data.to_csv('States_Left.csv')

screen.exitonclick()
