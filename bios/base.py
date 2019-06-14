from operations.standart_io import StandartIO

# File Formats

YAML_FILES = ['yaml', 'yml']
CSV_FILES = ['csv']
JSON_FILES = ['csv']
XML_FILES = ['xml']
STANDART_FILES = ['standart']

FILE_TYPES = [YAML_FILES, CSV_FILES, JSON_FILES, XML_FILES]

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

def read_standart(file_name):
    io_object = StandartIO()
    return io_object.read(file_name)
read_functions[STANDART_FILES[0]] = read_standart

# Main Function
def read(file_name, file_type='none'):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    return read_functions[file_type](file_name)

############################## WRITE #############################
write_functions = {}

def write_standart(file_name, data):
    io_object = StandartIO()
    return io_object.write(file_name, data)
write_functions[STANDART_FILES[0]] = write_standart

# Main Function
def write(file_name, data, file_type = 'none'):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    write_functions[file_type](file_name, data)

############################## APPEND #############################
append_functions = {}

def append_standart(file_name, data, line):
    io_object = StandartIO()
    io_object.append(file_name, data, line)
append_functions[STANDART_FILES[0]] = append_standart

# Main Function
def append(file_name, data, file_type='none', line=0):
    if file_type == 'none':
        file_type = determine_file_type(file_name)
    append_functions[file_type](file_name, data, line)