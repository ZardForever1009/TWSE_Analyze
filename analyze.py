from termcolor import colored


# class initialize
class Analyze:
    def __init__(self, info, stock_list, stock_data, result_list):
        self.result_list = result_list
        self.stock_list = stock_list
        self.stock_data = stock_data
        self.info = info

    def print_info(self):
        import os
        os.system('color')
        print(colored(self.info, 'yellow', attrs=['bold']))

    # read file data and store into list
    def open_file_read_data(self):
        data_file_counter = 0
        for stock in self.stock_list:
            file_path = "C:\\Users\\user\\Desktop\\Stock\\Data\\" + str(stock) + ".csv"
            try:
                open(file_path, "r")
            except OSError:
                print(colored(">> fail to open " + str(stock) + " file\n", 'red'))
            f = open(file_path, "r")
            for line in f:
                self.stock_data[data_file_counter].append(line)
            f.close()
            data_file_counter += 1

    # print file data array to check if anything wrong
    def print_specified_data(self, n):
        print(">> This is the " + str(n) + "-th item in stock_data list\n")
        for data in self.stock_data[n]:
            print("--> " + str(data))
