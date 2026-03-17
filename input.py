# Simple Health Tracker Program

print("Welcome to Health Tracker")

# Take input from user
steps = int(input("Enter number of steps you walked today: "))
water = int(input("Enter glasses of water you drank today: "))

# Logic for steps
if steps >= 10000:
    print("Great job! You are very active today 💪")
else:
    print("Try to walk more. Aim for at least 10,000 steps 🚶")

# Logic for water
if water >= 8:
    print("Good hydration! Keep it up 💧")
else:
    print("Drink more water! Stay hydrated 💧")

# Final suggestion
if steps >= 10000 and water >= 8:
    print("Excellent! You are maintaining a healthy lifestyle 🎉")
else:
    print("Small improvements can make you healthier 👍")
