import pandas

data=pandas.read_csv("50_states.csv")
state="Ohio"
x_cor=data[data.state==state].x
print(type(x_cor))
# print(x_cor)
