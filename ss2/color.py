#1.1
color_list = ['Blue','Red','Black','Pink','Brown','Yellow']

#1.2
print("color_list at index 3:",color_list[3])

#1.3
i = int(input("Enter a number from 0-5: "))
print("Your color:",color_list[i])

#1.4
print(color_list)
for c in range(len(color_list)):
    print(color_list[c])

#1.5
color = input("What is your favorite color?")
color_check=0
for x in range(len(color_list)):
    if color_list[x] != color:
        color_check += 1
    if color_list[x] == color:
        print("Your color is at index {0} in my list".format(color_list.index(color)))
    if color_check == 6:
        print("Sorry, I could not find your color")
