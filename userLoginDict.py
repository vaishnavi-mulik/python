#dictionary storing username:password
users={
    "alice":"password123",
    "bob":"secure456",
    "charlie":"qwerty789"
}

#simulate a login
username_input=input("Enter username:")
password_input=input("Enter password:")

#check login
if username_input in users:
    if users[username_input]==password_input:
        print("login successful!")
    else:
        print("incorrect password.")
else:
    print("user not found.")

#create whether dictionary ("london":23) ask user to enter city name and
#print result as london has 23 degree celcus now

weather={
    "london":23,
    "delhi":45,
    "mumbai":21
    }
city=input("enter a city name:")


if city in weather_data:
    print(f"{city}has {weather_data[city]}celsius right now.")
else:
    print("city not found in weather data.")
    
