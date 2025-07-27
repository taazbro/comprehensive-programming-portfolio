# Assignment: Rainfall 
# Name: Tanjim Ahmed Al Zabeer

import matplotlib.pyplot as plt

# Creating Function to read rainfall data from the file. 

def read_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        city = "Adina"  
        data = []
        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) == 2:
                try:
                    number = float(parts[1])
                    data.append(number)
                except:
                    pass
        return city, data

# creating Function to create line plot to diffrence between both data sets , Let's go

def plot_comparison(data1, data2):
    x = list(range(1, len(data1)+1))
    plt.figure()
    plt.plot(x, data1, color="blue", label="Set 1")
    plt.plot(x, data2, color="red", label="Set 2")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (inches)")
    plt.title("Comparison of Rainfall Data")
    plt.legend()
    plt.savefig("comparison_plot.png")
    plt.close()

# Creating Function to plot single dataset with maximun and minimum showed

def plot_with_extremes(data, name, line_color):
    x = list(range(1, len(data)+1))
    max_value = max(data)
    min_value = min(data)
    max_index = data.index(max_value)
    min_index = data.index(min_value)

    plt.figure()
    plt.plot(x, data, color=line_color)
    plt.scatter([max_index+1], [max_value], color="green", label="Max")
    plt.scatter([min_index+1], [min_value], color="purple", label="Min")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (inches)")
    plt.title(name + " Rainfall")
    plt.legend()
    plt.savefig(name + "_extremes.png")
    plt.close()

# Creating Function to draw bar chart for average rainfall , rainy rainy

def plot_average_bar(data1, data2):
    avg1 = sum(data1) / len(data1)
    avg2 = sum(data2) / len(data2)

    plt.figure()
    plt.bar(["Set1", "Set2"], [avg1, avg2], color=["blue", "red"])
    plt.ylabel("Avg Rainfall (inches)")
    plt.title("Average Rainfall of Two Sets")
    plt.savefig("average_comparison.png")
    plt.close()

# We are going to start the main program here

def main():
    city1, set1 = read_data("rainfallISet1.txt")
    city2, set2 = read_data("rainfallSet2.txt")

    print("City Name from Set 1:", city1)

    plot_comparison(set1, set2)
    plot_with_extremes(set1, "Set1", "blue")
    plot_with_extremes(set2, "Set2", "red")
    plot_average_bar(set1, set2)

    

main()
