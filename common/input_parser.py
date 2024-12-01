import sys
import common


def read_lines_from_file(filename, strip=True):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines] if strip else [line.rstrip("\n") for line in lines]
        file.close()
    return lines


def read_script_arguments(argument_keywords):
    argument_to_value_map = {}
    if len(sys.argv) != len(argument_keywords) + 1 or sys.argv[1] == '':
        return argument_to_value_map
    for i in range(len(argument_keywords)):
        argument_to_value_map[argument_keywords[i]] = sys.argv[i + 1]
    return argument_to_value_map


def parse_arguments(arguments_keywords, error_info):
    script_arguments = read_script_arguments(arguments_keywords)
    if len(script_arguments) == 0:
        common.print_array_line_by_line(error_info)
        return None
    print(len(script_arguments))
    return script_arguments


def init_day(day):
    help_info = [
        f"Script is solving task {day} of advent of code 2022",
        "Arguments:",
        common.TAB + "input file"
    ]
    arguments_keywords = ["inputFile"]

    script_arguments = parse_arguments(arguments_keywords, help_info)
    if script_arguments is None:
        return None

    input_file_name = script_arguments["inputFile"]
    print("solving file: " + input_file_name)
    return read_lines_from_file(input_file_name)
