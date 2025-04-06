# Justin Marucci 
# Assignment 4.2
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

def get_weather_data():
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_highs(dates, highs):
    plt.clf()  # Clear the current figure
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def plot_lows(dates, lows):
    plt.clf()  # Clear the current figure
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def display_menu():
    print("\nTemperature Data Viewer")
    print("----------------------")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    return input("\nEnter your choice (1-3): ")

def main():
    dates, highs, lows = get_weather_data()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            plot_highs(dates, highs)
        elif choice == '2':
            plot_lows(dates, lows)
        elif choice == '3':
            print("\nThank you for using the Temperature Data Viewer. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
