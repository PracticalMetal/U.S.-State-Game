import turtle
import pandas

# creating screen
screen=turtle.Screen()
screen.screensize(canvheight=240,canvwidth=400)
screen.title("U.S. State Game")

# Adding a new shape
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 

# Taking user input

correct_ans=0
data=pandas.read_csv("50_states.csv")
answered_states=[]

while correct_ans<=50:
    user_ans=screen.textinput(title=f"{correct_ans} /50 states guessed", prompt="What's your guess?")
    user_ans=user_ans.capitalize()

    if user_ans=="Exit":
        break

    if user_ans in answered_states[::]:
        pass
    else:

    # Reading file from pandas

        for state in data.state:
            if state==user_ans:
                correct_ans+=1
                answered_states.append(state)
                # create a turtle object and send it to that coordinate
                screen.tracer(0)
                on_screen_text=turtle.Turtle()
                on_screen_text.hideturtle()
                on_screen_text.penup()
                x_cor=data[data.state==state].x
                y_cor=data[data.state==state].y
                on_screen_text.goto(x=int(x_cor),y=int(y_cor))
                on_screen_text.write(state, font=("Verdana",8, "normal"))
                screen.update()


# Creating a CSV to tell which states were missed out
missed_out_states=[]
for state in data.state:
    if state not in answered_states[::]:
        missed_out_states.append(state)

data_dict={
    "Missed out states": missed_out_states
}

new_data=pandas.DataFrame(data_dict)
new_data.to_csv("to_learn.csv")