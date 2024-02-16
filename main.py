import turtle
import pandas
print("AhmedAbdel Moneim Explained this project;")
screen = turtle.Screen() # Create A Screen;
screen.title("U.S. States Game")
image = "states.gif"
# ADD New Shape to turtle;
screen.addshape(image)
# Display the Shape;
turtle.shape(image)
#Read the csv File;
data = pandas.read_csv("50_states.csv")
"""
ToSelectColumn: Data.ColumnName;
"""
print("Print the pandas DataFrame:\n",data)
print("Print the FirstColumn:\n",data.state)
print("Print the SecondColumn:\n",data.x)
print("Print the ThirdColumn:\n",data.y)
"""Data.iloc[:].to_list()"""
print("First Row\n",data.iloc[0,:].to_list())
print("First Column\n",data.iloc[:,0].to_list())
"""
>>Convert the Data To DataType:List[];
data.ColumnName.To_List();
"""
all_states = data.state.to_list()
guessed_states = [] # States You Enter;

while len(guessed_states) < 50:
    # Display a Dialog box and get user Input;
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit": # If User Input Exit End the Program;
        missing_states = [] # States User Not Input;
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # Create Pandas.DataFrame(rows&Column);
        new_data = pandas.DataFrame(missing_states)
        # Save the PandasDataFrame-to-csv,-Files;
        new_data.to_csv("states_to_learn.csv")
        break # End the While Loops;
    if answer_state in all_states:
        # Add New Answer to Guessed_List;
        guessed_states.append(answer_state)
        t = turtle.Turtle() # Create Turtle;
        t.hideturtle() # Hide the turtle();
        t.penup() # No Animation;
        # Condition Check if Data.state in answer_state;
        state_data = data[data.state == answer_state]
        print("Check If data.state in answer_state:\n",data.state==answer_state)
        print("Print True Row:\n",data[data.state == answer_state])
        """>>Move the Turtle to the-Specified-Coordinates(X, Y)on the-Screen()<<"""
        t.goto(int(state_data.x), int(state_data.y))
        """>>Write Text At the current position of the turtle<<"""
        t.write(answer_state)
"""
While Loop replacement turtle.mainloop()
"""
######End#############


