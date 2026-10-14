line = input() #rosalind gives the input in one line
pieces = line.split() #splits the string into list of strings, save the split result
n = int(pieces[0])  # Converts the first string to an integer (number of months)
k = int(pieces[1])  # Converts the second string to an integer (offspring per pair)
previous_month = 1
current_month = 1 
for month in range(3, n+1): #calculate every month from 3 to n
    next_month = current_month + (k *previous_month) # Rabbits this month = last month's rabbits + (k × rabbits from two months ago)
    previous_month=current_month
    current_month=next_month # Shift the months forward for the next calculation.
print(current_month)