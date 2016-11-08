import age

user_age = input("Enter your age: ")
#new instance of Age object
age = age.Age(user_age)
#save to variable
age_in_seconds = age.age_to_seconds()

print("You have lived {} seconds").format(age_in_seconds)
