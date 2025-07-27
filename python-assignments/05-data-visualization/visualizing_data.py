import seaborn as sns
import matplotlib.pyplot as plt

# Activity days
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# My activity per day (in hours)
netflix_hours = [2, 1, 1.5, 2, 2.5, 3, 4]
leisure_time = [2, 1, 2, 1, 3, 2, 2]
school_hours = [0, 5, 0, 5, 3, 0, 0]
gaming_time = [0, 2, 0, 1.5, 3, 4, 3]
hacking_practice = [2, 3, 2, 1.5, 2, 2, 3]
personal_study = [3, 5, 3, 5, 3, 4, 6]

# We will Prepare the data here for the program
data = {
    "Day": days * 6,
    "Hours": (
        netflix_hours +
        leisure_time +
        school_hours +
        gaming_time +
        hacking_practice +
        personal_study
    ),
    "Activity": (
        ["Netflix"] * 7 +
        ["Leisure"] * 7 +
        ["School"] * 7 +
        ["Gaming"] * 7 +
        ["Hacking"] * 7 +
        ["Personal Study"] * 7
    )
}

# Creating barplot here to display
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x="Day", y="Hours", hue="Activity", data=data)

# We are going to Add titles and labels here
plt.title("Daily Time Spent on Activities")
plt.xlabel("Day of the Week")
plt.ylabel("Hours")

# It will now Save and display the result
plt.savefig("weekly_activities_full.png")
plt.show()

