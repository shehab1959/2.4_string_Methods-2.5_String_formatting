#2.5- String Formatting
a="Hello! Good Mornig, Rahim. How are you?"
print(a)

#Input From User
user_input = input("What's your name?\n")
a="Good morning,{}.How are you?".format(user_input)
#print(user_input)
print(a)


## Using Function
age = 25
f_name = "Hejbulla"
l_name = "Shehab"

txt1 = "Hello everyone, I am {f_name} {l_name}. I'm {age} years old.".format(f_name=f_name, l_name=l_name, age=age)
print(txt1)

txt2 = f"Hello everyone, I am {f_name} {l_name}. I'm {age} years old."
print(txt2)