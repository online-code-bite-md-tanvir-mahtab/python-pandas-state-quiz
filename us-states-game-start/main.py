from turtle import Turtle, Screen
import pandas
import csv
from Text import Text

# keeping the track of the score
score = 0
# creating the state list keeping data
correct_state_list = []
# to keep the state of a game
is_game_over  = True
# to store the new data..
new_data = []

# creating the instace of the Turtle calss
tummy = Turtle()
# creating the insktance of fthe Screen class
screen = Screen()
# now i am going to read the csv file
data = pandas.read_csv('us-states-game-start/50_states.csv')


image = "us-states-game-start/blank_states_img.gif"
# now i need to add the shape
screen.addshape(image)
# now i am going to define a square shape
tummy.shape(image)


# now i am going to convert my data to dictionary
dict_data = data.to_dict()
# # print(dict_data)
# with open('s_data.txt',mode='w') as file:
#     file.write(str(dict_data))

text = Text()


list_data = data.state.to_list()
x_data = data.x.to_list()
y_data = data.y.to_list()


while is_game_over:
    quiz_len = len(list_data)
    correct =len(correct_state_list)
    # we also need to take the user input for that we are going to create the input box
    user_input = screen.textinput(title=f"{correct}/{quiz_len}",prompt="What's another state's name:")


    # print(list_data)
    # for item in list_data:
    if user_input == 'exit':
        if correct >0:
            for item in correct_state_list:
                if item in list_data:
                    # we are going to remove the data from the list
                    # then we are going to store them into a csv file

                    r_index = list_data.index(item)
                    list_data.remove(item)
                    x_data.remove(x_data[r_index])
                    y_data.remove(y_data[r_index])
                    new_data.append(list_data)
                    new_data.append(x_data)
                    new_data.append(y_data)
                    store = pandas.DataFrame(new_data)
                    store.to_csv('new_data.csv')
            print(r_index)
            print(f"the new data: {new_data} ")
        else:
            pass
        break
    elif user_input in list_data:
        index = list_data.index(user_input)
        score += 1
        text.make_text(user_input ,x=x_data[index],y=y_data[index])
        correct_state_list.append(user_input)



print(f"the score is : {score}")
print(f"the correct data is :{correct_state_list}")
print(f"the position is :{index}")


# to close the screen when the user clicked
screen.exitonclick()
