def remove_dollar_string(s):
    new_string = s.replace("$","")
    return new_string

string_with_no_dollars = remove_dollar_string("$80% percent of $life is showing $up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

