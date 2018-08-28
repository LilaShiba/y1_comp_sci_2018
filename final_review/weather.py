# Create a 2D array that contains days and a list of their
# Highest, lowest, and mean temp
# Then
# Cycle through this 2D array to
# Find the highest of all temps and return that day

#Data Type: Days => 0-6, Temps => 0-2
# Row = Day
# Col = Temp
# highest_temp = 0
# if weather[i][o] > highest_temp
# highest_temp = weather[i][o]


weather = [[64, 75, 81],[72, 76, 80],[90, 76, 73],[78, 72, 70],[82, 72, 77],[88, 80, 85]]
highest_temp = 0

# I iterate over row
for i in range(len(weather)):
    # J iterate over temps
    for j in range(len(weather[i])):
        if weather[i][j] > highest_temp:
            highest_temp = weather[i][j]
print(highest_temp)
