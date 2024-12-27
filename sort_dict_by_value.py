# Program to sort dictionary by value

d = {1:'grapes', 2:'banana', 3:'apples', 4:'figs'}

sorted_d = sorted(d.items(), key=lambda x: x[1])
print(sorted_d)

# sort only values
sorted_val = sorted(d.values())
print(sorted_val)


    