unit = input ("Enter unit to convert from [C, F, K]: ")
user_input = input ("Enter Temperature : ")

temp = float(user_input)

if unit == "C":
    C = temp
    F = (temp*9/5) + 32
    K = temp + 273
elif  unit == "F":
    C = (temp - 32) * 5/9
    F = temp
    K = 5/9 * (temp - 32) + 273
elif unit == "K":
    C = temp - 273
    F = 9/5*(temp - 273) + 32
    K = temp
else: 
    print("Invalid Unit")
    exit()
print( f" {temp} {unit} = {C} C\n")
print( f" {temp} {unit} = {F} F\n")
print( f" {temp} {unit} = {K} K\n")