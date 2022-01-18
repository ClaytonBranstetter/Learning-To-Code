# Obtain 100 numbers from the user (assume floating point values). You will then obtain a threshold value from the user and display all values above the threshold.

num_list = [float(input("Insert Number: ")) for i in range(100) ]
threshold = float(input("input threshold: "))
print([num for num in num_list if num > threshold])
