rain = input("Is it raining? (Yes/No): ").lower()
Humidity = int(input("Humidity (0-100): "))
windspeed = int(input("Wind speed (km/hr): "))


if (rain == "Yes,yes"):
    print("We will NOT PLAY tennis.")
elif (Humidity <= 65 or windspeed <= 5):
    print("We will NOT PLAY tennis.")
else:
    print("We will PLAY tennis.")

