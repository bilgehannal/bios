# bios

  - 'bios' is a python library which helps you for operations of I/O.
  - You can read determined type of files and assign the content of the files to the best suitable data type for these contents.
  - If it is required, developer should handle the exception handling issues.

### Install and Import

> pip install bios

    import bios

### Supported Files
 - JSON Files
	 - Can be assigned to data types of string, list or dict.
 - YAML Files
	 - Can be assigned to data types of string, list or dict.
 - CSV Files
	 - Can be assigned to data types of string or list.
 - Other Files
	- Can be assigned to data type of string.

### Operations and Using

#### Reading
You can read the file using read function of bios. If you will not give any file type, system can determined the file types showing in the below and assign the content of the files to suitable data_types.

    content1 = bios.read('file.txt')
    content2 = bios.read('file.json')
    content3 = bios.read('file.yaml')
    content4 = bios.read('file.csv')
    content4 = bios.read('file.csv', delimiter=';')
    content5 = bios.read('file.yml')
    content6 = bios.read('file')

	# Type of content1 and contend6 is string
	# Type of content2, content3 and content5 is dict or list
	# Tyoe of content4 is list

- ##### Standart File

You can read the content of a file and assign it into a string.

    content = bios.read('file.txt', file_type='standart')

- ##### JSON File

You can read the content of a JSON file and assign it into a dict or list object.

    content = bios.read('file.json', file_type='json')

Type of the content could be 'list' or 'dict'
- ##### YAML File

You can read the content of a YAML file and assign it into a dict or list object.

    content = bios.read('file.yaml', file_type='yaml')
    content = bios.read('file.yaml', file_type='yml')

Type of the content could be 'list' or 'dict'
- ##### CSV File

You can read the content of a CSV file and assign it into a list. Default delimiter is comma ' , '.

    content = bios.read('file.json', file_type='csv')
	content = bios.read('file.json', file_type='csv', delimiter=';')

Type of the content could be 'list'

#### Writing
You can write your 'data' object to a file. If you will not give a specific file a file type, file type is determined according to the file name.

    bios.write('file.txt', data1)
    bios.write('file.json', data2)
    bios.write('file.yaml', data3)
    bios.write('file.csv', data4)
    bios.write('file.csv', data4, delimiter=';')
    bios.write('file.yml', data5)
    bios.write('file', data5)
	
	# data1 and data5 must be a string
	# data2, data3 and data5 must be a dict or list object
	# data4 must be a list object
	
- ##### Standart File

You can write a string object to any file giving a file type as 'standart'

     bios.write('file.txt', data, file_type='standart')

- ##### JSON File

You can write a list or dict object to any file giving a file type as 'json'

     bios.write('file.json', data, file_type='json')
     
- ##### YAML File

You can write a list or dict object to any file giving a file type as 'yaml' or 'yml'

     bios.write('file.yml', data, file_type='yaml')
     
- ##### CSV File

You can write a list object to any file giving a file type as 'standart'

     bios.write('file.csv', data, file_type='csv')
     bios.write('file.csv', data, file_type='csv', delimiter=';')

You can use the parameter of 'delimiter' for separating the contents from each other.
     
#### Appending
You can append or add a content to an existing file. This function is available for only text files or csv files.

    bios.append('file.txt', data)
    bios.append('file.txt', data, line=2)
    bios.append('file.txt', data, delimiter=';')
    bios.append('file.csv', data, line=2, delimiter=';')
    
Line is assumed that starting from the value of 1

- ##### Standart File

You can append a string object to a existing or nonexistent file. If you don't give a line parameter, bios would append the content after the end of the file.

     bios.append('file.txt', data, file_type='standart')
     bios.append('file.txt', data, file_type='standart', line=2)

- ##### CSV File

You can append a list object to a existing or nonexistent file. If you don't give a line parameter, bios would append the content after the end of the file.

     bios.append('file.csv', data, file_type='csv')
     bios.append('file.csv', data, file_type='csv', line=2)

###  Example

    import bios
    content = bios.read('files/my_file.csv')
    second_row = content[1]
    for single_column in second_row:
	    print(single_column)
  