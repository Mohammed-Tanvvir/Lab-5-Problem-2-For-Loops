print("⌚Welcome to the Timer⌚")

hour = 00
min = 00
seconds = 00

for hour in range(24):
    for min in range(60):
        for seconds in range(60):
            print(f"{hour:02}:{min:02}:{seconds:02}")
