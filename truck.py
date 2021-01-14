from datetime import datetime, timedelta
from math import ceil

TRAVEL_SPEED = 18.0
LOAD_CAPACITY = 16
END_OF_DAY = datetime.strptime('18:00:00', '%H:%M:%S')
START_OF_DAY = datetime.strptime('08:00:00', '%H:%M:%S')


# This class creates a Truck object which holds package objects in a truck_manifest list and keeps track of current
# location and time for updating package statuses and calculating distances. Notice I did not add an attribute for
# drivers (There are only 2). This could be easily implemented at a later date, but for this specific project I accounted
# for the trucks' time delivering with plenty of time to spare.
class Truck:
    # O(1) complexity
    def __init__(self, truck_id = 1):
        self.truck_id = truck_id
        self.number_of_packages = 0
        self.truck_manifest = []
        self.current_location = '4001 South 700 East'
        self.miles_travelled_today = 0.0
        self.next_package = None
        if self.truck_id == 1:
            self.current_time = START_OF_DAY
        elif self.truck_id == 2:
            self.current_time = datetime.strptime('09:05:00', '%H:%M:%S')
        elif self.truck_id == 3:
            self.current_time = datetime.strptime('12:00:00', '%H:%M:%S')

# This method manually loads all packages onto 3 trucks. O(N) complexity
    @staticmethod
    def load_truck(delivery_truck, all_packages):
        truck1_packages = ['37', '2', '4', '7', '8', '13', '14', '15', '16', '19', '20', '29', '30', '33', '34', '40']
        truck2_packages = ['3', '5', '6', '12', '17', '18', '21', '25', '26', '28', '31', '32', '36', '1', '38']
        truck3_packages = ['10', '11', '22', '23', '24', '27', '35', '39', '9']

        for package in all_packages:
            if delivery_truck.truck_id == 1 and package.package_info[0] in truck1_packages:
                delivery_truck.truck_manifest.append(package)
                delivery_truck.number_of_packages += 1
            elif delivery_truck.truck_id == 2 and package.package_info[0] in truck2_packages:
                delivery_truck.truck_manifest.append(package)
                delivery_truck.number_of_packages += 1
            elif delivery_truck.truck_id == 3 and package.package_info[0] in truck3_packages:
                delivery_truck.truck_manifest.append(package)
                delivery_truck.number_of_packages += 1

# This method calculates the time a truck takes to travel a distance in minutes adds that calculation to the truck's time.
# O(1) complexity
    def add_traveling_time(self, distance):
        time_traveled = ceil((distance / TRAVEL_SPEED) * 60)
        self.current_time += timedelta(minutes = time_traveled)
