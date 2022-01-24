from analyze import Analyze

stock_list = ["2408", "2436", "2449", "3035", "3532", "3583"]
analyze_tool = Analyze("\n=====TWSE Stock Reverse Point Analyzer=====\n", stock_list, [[], [], [], [], [], []], [])

analyze_tool.print_info()
analyze_tool.open_file_read_data()
analyze_tool.parse_data_and_analyze()
analyze_tool.print_result()