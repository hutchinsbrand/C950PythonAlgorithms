import csv
from package import Package


# This class uses the packages_list and distances_list csv files to initialize and populate 3 lists used elsewhere in
# the program.
class Upload:
    def __init__(self):
        self.all_packages = []
        self.all_distances = []
        self.all_addresses = []
# O(N) complexity
        with open('packages_list.csv') as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')

            for row in read_csv:
                package_num = row[0]
                package_street_address = row[1]
                package_city = row[2]
                package_state = row[3]
                package_zip_code = row[4]
                package_deliver_by = row[5]
                package_weight = row[6]
                package_special_notes = row[7]
                package_status = 'At Hub'
                package_info = [package_num, package_street_address, package_city, package_state, package_zip_code, package_deliver_by, package_weight, package_special_notes, package_status]
                new_package = Package(package_info)
                self.all_packages.append(new_package)

# O(N) complexity
        with open('distances_list.csv') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')

            i = 1
            j = 0
            distances = []

            for row in readCSV:
                row = [char.replace('\n', ' ') for char in row]

                if (i - 1) == 0:
                    self.all_addresses = row

                distances.append(row[1:(len(row) - (len(row) - i))])
                i += 1

            self.all_addresses.pop(0)

            for address in self.all_addresses:
                self.all_distances.append((address, distances[j + 1]))
                j += 1
