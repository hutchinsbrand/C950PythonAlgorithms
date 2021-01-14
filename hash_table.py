# This class builds a chaining hash table to store all packages imported from the csv file for the day.
# It contains a linear search function (PART F) and insert function (PART E).
# I defaulted table size to 40 to keep things simple for this particular case, but this can be adjusted as scaling needs require.


class HashTable:
    # O(N) complexity
    def __init__(self, table_size = 40):
        self.hash_table = []
        self.bucket_destination = 0
        i = 0
        while i < table_size:
            self.hash_table.append([])
            i += 1

    # Currently hashing method results in (what could be) a Direct Addressing Table but is a chaining hash table of a
    # table size given at initialization. O(1) complexity
    def hashing(self, package, table_size = 40):
        self.bucket_destination = (int(package.package_info[0]) % table_size) - 1

    # O(1) complexity
    def insert_package(self, package):
        self.hash_table[self.bucket_destination].append(package)

    # O(N) complexity
    def del_package(self, package):
        for lists in self.hash_table:
            if package in lists:
                lists.remove(package)

    # O(N^2) complexity
    def search_hash_table(self, package_num):
        for lists in self.hash_table:
            for package in lists:
                if package.package_info[0] == package_num:
                    return package
