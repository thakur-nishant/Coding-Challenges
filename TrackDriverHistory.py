"""
Let's write some code to track driving history for people.

The code will process an input file. You can either choose to accept the input via stdin (e.g. if you're using Ruby cat input.txt | ruby yourcode.rb), or as a file name given on the command line (e.g. ruby yourcode.rb input.txt). You can use any programming language that you want. Please choose a language that allows you to best demonstrate your programming ability.

Each line in the input file will start with a command. There are two possible commands.

The first command is Driver, which will register a new Driver in the app. Example:

Driver Dan

The second command is Trip, which will record a trip attributed to a driver. The line will be space delimited with the following fields: the command (Trip), driver name, start time, stop time, miles driven. Times will be given in the format of hours:minutes. We'll use a 24-hour clock and will assume that drivers never drive past midnight (the start time will always be before the end time). Example:

Trip Dan 07:15 07:45 17.3

Discard any trips that average a speed of less than 5 mph or greater than 100 mph.

Generate a report containing each driver with total miles driven and average speed. Sort the output by most miles driven to least. Round miles and miles per hour to the nearest integer.

Example input:

Driver Dan
Driver Alex
Driver Bob
Trip Dan 07:15 07:45 17.3
Trip Dan 06:12 06:32 21.8
Trip Alex 12:01 13:16 42.0
Expected output:

Alex: 42 miles @ 34 mph
Dan: 39 miles @ 47 mph
Bob: 0 miles
"""
from datetime import datetime

class TrackDriver:
    def __init__(self,filename):
        input_data = self.read_file(filename)
        self.keep_track(input_data)

    #function to read the data from a given file
    def read_file(self, filename):
        input_data = []
        with open(filename) as f:
            for line in f:
                input_data.append(line)
        return input_data

    # function to calculate speed
    def calculate_speed(self, total_time, total_distance):
        if total_time:
            return total_distance / total_time
        else:
            return 0

    # function to calculate the difference between start and end time of trip i.e. trip time
    def calculate_trip_time(self, start, end):
        t_diff = datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')
        temp = str(t_diff).split(':')
        trip_time =  int(temp[0]) + (int(temp[1])/60)
        return trip_time

    # function to print the history of drivers
    def print_output(self, history):
        sorted_drivers = sorted(history,key = history.__getitem__, reverse = True)
        for driver in sorted_drivers:
            driver_name = driver
            total_distance = int(round(history[driver][0]))
            average_speed = int(round(self.calculate_speed(history[driver][1],history[driver][0])))
            if total_distance:
                print(driver_name + ": " + str(total_distance) + " miles @ " + str(average_speed) + " mph")
            else:
                print(driver_name + ": 0 miles")

    # function to track history of drivers
    def keep_track(self, data):
        history = {}
        # for each record form history
        for line in data:
            ip = line.split()
            # add driver to history if it doesn't exist.
            if ip[0] == "Driver" and ip[0] not in history:
                history[ip[1]] = [0,0]
            elif ip[0] == "Trip":
                total_time = self.calculate_trip_time(ip[2], ip[3])
                distance = float(ip[4])
                driver = ip[1]
                speed = self.calculate_speed(total_time, distance)
                # if the driver is available in history
                if driver in history and speed >= 5 and speed <= 100:
                    history[driver][0] += distance
                    history[driver][1] += total_time
        # call function to print the output
        self.print_output(history)


if __name__ == "__main__":
    filename = "input.txt"
    x = TrackDriver(filename)
