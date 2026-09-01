rain = input("Is it raining? (Yes/No): ").lower()
humidity = float(input("Humidity (0-100): "))
windspeed = float(input("Wind speed (km/hr): "))

if rain in ("yes", "y"):
    print("We will NOT play tennis.")
elif humidity <= 65 or windspeed <= 5:
    print("We will PLAY tennis.")
else:
    print("We will NOT play tennis.")

#Finished