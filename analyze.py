import os
from termcolor import colored
from time import sleep


# class initialize
class Analyze:
    def __init__(self, info, stock_list, stock_data, result_list):
        self.result_list = result_list
        self.stock_list = stock_list
        self.stock_data = stock_data
        self.info = info

    def print_info(self):
        os.system('color')
        print(colored(self.info, 'yellow', attrs=['bold']))

    # read file data and store into list
    def open_file_read_data(self):
        data_file_counter = 0
        print(colored(">> Start file data reading", 'yellow', attrs=['bold']))
        for stock in self.stock_list:
            file_path = "C:\\Users\\user\\Desktop\\Stock\\Data\\" + str(stock) + ".csv"
            print(colored(">> Trying to read " + str(stock) + " files", 'yellow'))
            try:
                open(file_path, "r")
            except OSError:
                print(colored(">> fail to open " + str(stock) + " file\n", 'red'))
            f = open(file_path, "r")
            print(colored(">> Successfully reading " + str(stock) + " files", 'green'))
            for line in f:
                self.stock_data[data_file_counter].append(line)
            f.close()
            data_file_counter += 1
            sleep(1)
        print(colored(">> All files reading are done", 'yellow', attrs=['bold']))

    # print file data array to check if anything wrong
    def print_specified_data(self, n):
        print(">> This is the " + str(n) + "-th item in stock_data list\n")
        for data in self.stock_data[n]:
            print("--> " + str(data))

    # parse data and analyze
    def parse_data_and_analyze(self):
        print(colored("\n>> Start week data parsing", 'yellow', attrs=['bold']))
        print(colored(">> Parsing data...", 'green'))
        sleep(2)
        # initialize soe list to store week data ready for analyze
        five_week_ago_high = []
        five_week_ago_low = []
        four_week_ago_high = []
        four_week_ago_low = []
        three_week_ago_high = []
        three_week_ago_low = []
        two_week_ago_high = []
        two_week_ago_low = []
        one_week_ago_high = []
        one_week_ago_low = []
        this_week_high = []
        this_week_low = []
        for single_stock_data in self.stock_data:
            count_week = 1
            sleep(1)
            for single_week_data in single_stock_data:
                print(count_week)
                if count_week > (len(single_stock_data) - 6):
                    s = single_week_data.split('/')
                    if count_week == len(single_stock_data) - 5:
                        print(">> five:" + str(five_week_ago_high) + "/" + str(five_week_ago_low))
                        five_week_ago_high.append(s[1])
                        five_week_ago_low.append(s[2])
                        count_week += 1
                    elif count_week == len(single_stock_data) - 4:
                        print(">> four:" + str(four_week_ago_high) + "/" + str(four_week_ago_low))
                        four_week_ago_high.append(s[1])
                        four_week_ago_low.append(s[2])
                        count_week += 1
                    elif count_week == len(single_stock_data) - 3:
                        print(">> three:" + str(three_week_ago_high) + "/" + str(three_week_ago_low))
                        three_week_ago_high.append(s[1])
                        three_week_ago_low.append(s[2])
                        count_week += 1
                    elif count_week == len(single_stock_data) - 2:
                        print(">> two:" + str(two_week_ago_high) + "/" + str(two_week_ago_low))
                        two_week_ago_high.append(s[1])
                        two_week_ago_low.append(s[2])
                        count_week += 1
                    elif count_week == len(single_stock_data) - 1:
                        print(">> one:" + str(one_week_ago_high) + "/" + str(one_week_ago_low))
                        one_week_ago_high.append(s[1])
                        one_week_ago_low.append(s[2])
                        count_week += 1
                    elif count_week == len(single_stock_data):
                        print(">> now:" + str(this_week_high) + "/" + str(this_week_low))
                        this_week_high.append(s[1])
                        this_week_low.append(s[2])
                        count_week += 1
                else:
                    count_week += 1
            print("=============================================")
        print(colored(">> Almost there...", 'green'))
        sleep(2)
        print(colored(">> Week data parsing completely\n", 'yellow', attrs=['bold']))
        print(colored(">> Start data analyzing", 'yellow', attrs=['bold']))
        for i in range(0, 6):
            print(colored(">> Stock " + str(self.stock_list[i]) + " analyzing", 'green'))
            if self.reverse_in_three_weeks(float(this_week_high[i]), float(this_week_low[i]), float(one_week_ago_high[i]), float(one_week_ago_low[i]), float(two_week_ago_high[i]),
                                           float(two_week_ago_low[i])):
                self.result_list.append(True)
            elif self.reverse_in_four_weeks(float(this_week_high[i]), float(this_week_low[i]), float(one_week_ago_high[i]), float(one_week_ago_low[i]), float(two_week_ago_high[i]),
                                            float(two_week_ago_low[i]),
                                            float(three_week_ago_high[i]),
                                            float(three_week_ago_low[i])):
                self.result_list.append(True)
            elif self.reverse_in_five_weeks(float(this_week_high[i]), float(this_week_low[i]), float(one_week_ago_high[i]), float(one_week_ago_low[i]), float(two_week_ago_high[i]),
                                            float(two_week_ago_low[i]),
                                            float(three_week_ago_high[i]),
                                            float(three_week_ago_low[i]), float(four_week_ago_high[i]), float(four_week_ago_low[i])):
                self.result_list.append(True)
            elif self.reverse_in_six_weeks(float(this_week_high[i]), float(this_week_low[i]), float(one_week_ago_high[i]), float(one_week_ago_low[i]), float(two_week_ago_high[i]),
                                           float(two_week_ago_low[i]),
                                           float(three_week_ago_high[i]),
                                           float(three_week_ago_low[i]), float(four_week_ago_high[i]), float(four_week_ago_low[i]), float(five_week_ago_high[i]), float(five_week_ago_low[i])):
                self.result_list.append(True)
            else:
                self.result_list.append(False)
            sleep(1)
        print(colored(">> Finish data analyzing\n", 'yellow', attrs=['bold']))

    def print_result(self):
        print(colored("=====Final Reverse Point Result=====\n", 'yellow', attrs=['bold']))
        for i in range(0, 6):
            output = str(self.stock_list[i]) + " >> "
            if self.result_list[i]:
                print(output + colored("True", 'green', attrs=['bold']))
            else:
                print(output + colored("False", 'red'))
        print(colored("====================================\n", 'yellow', attrs=['bold']))
        os.system('pause')

    # find the reverse points which occurred within three weeks
    def reverse_in_three_weeks(self, this_week_high, this_week_low, one_week_ago_high, one_week_ago_low, two_week_ago_high, two_week_ago_low):
        if this_week_high > one_week_ago_high and this_week_low > one_week_ago_low:
            if two_week_ago_high > one_week_ago_high and two_week_ago_low > one_week_ago_low:
                return True
            else:
                return False
        else:
            return False

    def reverse_in_four_weeks(self, this_week_high, this_week_low, one_week_ago_high, one_week_ago_low, two_week_ago_high, two_week_ago_low, three_week_ago_high, three_week_ago_low):
        if this_week_high > two_week_ago_high and this_week_low > two_week_ago_low:
            if three_week_ago_high > two_week_ago_high and three_week_ago_low > two_week_ago_low:
                if one_week_ago_low > two_week_ago_low and one_week_ago_high < two_week_ago_high:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def reverse_in_five_weeks(self, this_week_high, this_week_low, one_week_ago_high, one_week_ago_low, two_week_ago_high, two_week_ago_low, three_week_ago_high, three_week_ago_low,
                              four_week_ago_high, four_week_ago_low):
        if this_week_high > three_week_ago_high and this_week_low > three_week_ago_low:
            if four_week_ago_high > three_week_ago_high and four_week_ago_low > three_week_ago_low:
                if one_week_ago_low > three_week_ago_low and one_week_ago_high < three_week_ago_high:
                    if two_week_ago_low > three_week_ago_low and two_week_ago_high < three_week_ago_high:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def reverse_in_six_weeks(self, this_week_high, this_week_low, one_week_ago_high, one_week_ago_low, two_week_ago_high, two_week_ago_low, three_week_ago_high, three_week_ago_low, four_week_ago_high,
                             four_week_ago_low, five_week_ago_high, five_week_ago_low):
        if this_week_high > four_week_ago_high and this_week_low > four_week_ago_low:
            if five_week_ago_high > four_week_ago_high and five_week_ago_low > four_week_ago_low:
                if one_week_ago_low > four_week_ago_low and one_week_ago_high < four_week_ago_high:
                    if two_week_ago_low > four_week_ago_low and two_week_ago_high < four_week_ago_high:
                        if three_week_ago_low > four_week_ago_low and three_week_ago_high < four_week_ago_high:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
