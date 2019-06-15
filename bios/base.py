from bios.operations.standart_io import StandartIO
from bios.operations.csv_io import CsvIO

# File Formats

YAML_FILES = ['yaml', 'yml']
CSV_FILES = ['csv']
JSON_FILES = ['json']
STANDART_FILES = ['standart']

FILE_TYPES = [YAML_FILES, CSV_FILES, JSON_FILES]

# Key Determiner
def determine_file_type(file_name):
    file_name_array = file_name.split('.')
    if len(file_name_array) > 1:
        taken_file_type = file_name_array[-1]
        for file_type in FILE_TYPES:
            for variation_of_file_type in file_type:
                if variation_of_file_type == taken_file_type:
                    return file_type[0]
    return STANDART_FILES[0] 


############################## READ #############################
read_functions = {}

def read_standart(file_name, delimiter):
    io_object = StandartIO()
    return io_object.read(file_name)
read_functions[STANDART_FILES[0]] = read_standart

def read_csv(file_name, delimiter):
    io_object = CsvIO()
    return io_object.read(file_name, delimiter)
read_functions[CSV_FILES[0]] = read_csv

# Main Function
def read(file_name, file_type='none', delimiter=','):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    return read_functions[file_type](file_name, delimiter)

############################## WRITE #############################
write_functions = {}

def write_standart(file_name, data, delimiter):
    io_object = StandartIO()
    io_object.write(file_name, data)
write_functions[STANDART_FILES[0]] = write_standart

def write_csv(file_name, data, delimiter):
    io_object = CsvIO()
    io_object.write(file_name, data, delimiter)
write_functions[CSV_FILES[0]] = write_csv

# Main Function
def write(file_name, data, file_type = 'none', delimiter=','):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    write_functions[file_type](file_name, data, delimiter)

############################## APPEND #############################
append_functions = {}

def append_standart(file_name, data, line, delimiter):
    io_object = StandartIO()
    io_object.append(file_name, data, line)
append_functions[STANDART_FILES[0]] = append_standart

def append_csv(file_name, data, line, delimiter):
    io_object = CsvIO()
    io_object.append(file_name, data, line, delimiter)
append_functions[CSV_FILES[0]] = append_standart

# Main Function
def append(file_name, data, file_type='none', line=0, delimeter=','):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    append_functions[file_type](file_name, data, line, delimeter)