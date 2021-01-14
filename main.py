from hash_table import HashTable
from truck import *
from upload_data import Upload


# Name: Brandon Hutchinson ### Student ID: 001282535

# This class contains the main method which initializes all required objects O(N) and the user interface
class Main:
    @staticmethod
    def main():
        truck_1 = Truck(1)
        truck_2 = Truck(2)
        truck_3 = Truck(3)
        data_today = Upload()
        Truck.load_truck(truck_1, data_today.all_packages)
        Truck.load_truck(truck_2, data_today.all_packages)
        Truck.load_truck(truck_3, data_today.all_packages)
        all_trucks = [truck_1, truck_2, truck_3]
        table = HashTable()

# This creates user interface and its functionality on command line. Big O is O(N) complexity.
        for package in data_today.all_packages:
            table.hashing(package)
            table.insert_package(package)
        total_mileage = Main.delivery_algorithm(all_trucks, data_today.all_distances, table.hash_table)
        user_selected = '0'
        while user_selected != '4':
            print('---WGUPS Package Tracking---')
            print('\n')
            print('1 -- Search for an individual package')
            print('2 -- Print all packages (at a chosen time)')
            print('3 -- Get total mileage for today\'s deliveries')
            print('4 -- End session')
            print('\n')
            user_selected = input('Please select a number for an option from above: ')
            print('\n')
            if user_selected == '1':
                package_to_retrieve = input('Please enter a package number who\'s status you want to check: ')
                if not package_to_retrieve.isnumeric():
                    print('Please enter your number in numeric form (e.g. 1, 2, 3).')
                    print('\n')
                    continue
                time_to_check = input('Please enter a time to check package\'s status at (HH:MM:SS): ')
                time_format = '%H:%M:%S'
                print('\n')
                if len(time_to_check) != 8:
                    print('Please make sure the time you entered is formatted correctly, and try again.')
                    print('\n')
                    continue
                try:
                    datetime.strptime(time_to_check, time_format)
                except ValueError:
                    print('Please make sure the time you entered is formatted correctly, and try again.')
                    print('\n')
                    continue
                Main.check_package_status(package_to_retrieve, time_to_check, table)
            elif user_selected == '2':
                time_to_check = input('Please enter a time to check packages\' statuses at (HH:MM:SS): ')
                time_format = '%H:%M:%S'
                print('\n')
                try:
                    datetime.strptime(time_to_check, time_format)
                except ValueError:
                    print('Please make sure the time you entered is formatted correctly, and try again.')
                    print('\n')
                    continue
                Main.check_all_package_statuses(time_to_check, table)
            elif user_selected == '3':
                print('Today\'s total miles: ', total_mileage)

        print('...Closing Session...')

# See the attached Documentation for a comprehensive breakdown on this algorithm. In short, it is a greedy algorithm
# with some modifications to meet all special requirements for delivery. O(N^3) complexity
    @staticmethod
    def delivery_algorithm(all_loaded_trucks, all_distances, hash_table):
        total_miles_all_trucks = 0
        for truck in all_loaded_trucks:
            while truck.number_of_packages > 0:
                min_distance = 100.0
                for package in truck.truck_manifest:
                    if (package.package_info[0] == '9') and (str(truck.current_time) > '10:20:00'):
                        package.package_info[1] = '410 S State St'
                        package.package_info[4] = '84111'
                        hash_table[int(package.package_info[0]) - 1][0].package_info[1] = '410 S State St'
                        hash_table[int(package.package_info[0]) - 1][0].package_info[4] = '84111'
                    if Main.distance_between(truck, package.package_info[1], all_distances) < min_distance:
                        min_distance = Main.distance_between(truck, package.package_info[1], all_distances)
                        truck.next_package = package
                    if (package is truck.truck_manifest[len(truck.truck_manifest) - 1]) and (truck.current_location != truck.next_package.package_info[1]):
                        truck.current_location = truck.next_package.package_info[1]
                        truck.miles_travelled_today += min_distance
                        truck.add_traveling_time(min_distance)
                        hash_table[int(truck.next_package.package_info[0]) - 1][0].package_info[8] = 'Delivered at: ' + str(truck.current_time.time())
                        truck.truck_manifest.remove(truck.next_package)
                        truck.number_of_packages -= 1
                    elif package is truck.truck_manifest[len(truck.truck_manifest) - 1]:
                        truck.truck_manifest.remove(truck.next_package)
                        truck.number_of_packages -= 1
                        hash_table[int(truck.next_package.package_info[0]) - 1][0].package_info[8] = 'Delivered at: ' + str(truck.current_time.time())
            truck.miles_travelled_today += Main.distance_between(truck, '4001 South 700 East', all_distances)
            total_miles_all_trucks += truck.miles_travelled_today
        return total_miles_all_trucks

    # This method is called by delivery algorithm to return the distance between the truck and an address. O(N) complexity
    @staticmethod
    def distance_between(delivery_truck, address, all_distances):
        start_index = 0
        end_index = 0

        calculated_distance = 0.0
        for item in all_distances:
            if delivery_truck.current_location in item[0]:
                start_index = all_distances.index(item)
            if address in item[0]:
                end_index = all_distances.index(item)
        if end_index < start_index:
            calculated_distance = float(all_distances[start_index][1][end_index])
        elif start_index < end_index:
            calculated_distance = float(all_distances[end_index][1][start_index])
        elif start_index == end_index:
            pass
        else:
            print('There has been an error! Please notify your supervisor!')
        return calculated_distance

    # This method manually checks hash_table for a given package at a given time to determine its delivery status
    # and return it along with the package's information. O(1) complexity
    @staticmethod
    def check_package_status(package_num, time, table):

        truck_1_package_numbers = ['37', '2', '4', '7', '8', '13', '14', '15', '16', '19', '20', '29', '30', '33', '34', '40']
        truck_2_package_numbers = ['3', '5', '6', '12', '17', '18', '21', '25', '26', '28', '31', '32', '36', '1', '38']
        truck_3_package_numbers = ['10', '11', '22', '23', '24', '27', '35', '39', '9']
        retrieved_package = table.search_hash_table(package_num)
        depart_time = ''
        if time < '10:20:00' and package_num == '9':
            retrieved_package.package_info[1] = '300 State St'
            retrieved_package.package_info[4] = '84103'
        elif package_num == '9':
            retrieved_package.package_info[1] = '410 S State St'
            retrieved_package.package_info[4] = '84111'
        if retrieved_package.package_info[0] in truck_1_package_numbers:
            depart_time = '08:00:00'
        elif retrieved_package.package_info[0] in truck_2_package_numbers:
            depart_time = '09:05:00'
        elif retrieved_package.package_info[0] in truck_3_package_numbers:
            depart_time = '12:00:00'
        end_status_package = retrieved_package.package_info[8].split()
        if depart_time < time < end_status_package[2]:
            print(retrieved_package.package_info[0:8], 'Package is en route.')
            print('\n')
        elif time <= depart_time:
            print(retrieved_package.package_info[0:8], 'Package is at hub.')
            print('\n')
        elif time >= end_status_package[2]:
            print(retrieved_package.package_info[0:8], retrieved_package.package_info[8])
            print('\n')

    # This method takes the above method and applies it to the entire hash table, returning all packages and their statuses. O(N^2) complexity
    @staticmethod
    def check_all_package_statuses(time, table):
        for lists in table.hash_table:
            for package in lists:
                Main.check_package_status(package.package_info[0], time, table)


Main.main()
