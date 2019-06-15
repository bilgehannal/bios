
class CsvIO:

    def read(self, file_name, delimiter):
        content = []
        with open(file_name, 'r') as f:
            content = f.readlines()
        result = [x.strip().split(delimiter) for x in content]
        return result

    def write(self, file_name, data, delimiter):
        f = open(file_name, "w")
        result = ''
        for data_row in data:
            for data_column in data_row:
                result += data_column + delimiter
            result += '\n'
        result = result.strip()
        f.write(result)
        f.close()

    def append(self, file_name, data, line, delimiter):
        content = ''
        with open(file_name, 'r') as f:
            content = f.readlines()
        result = ''
        for data_column in data:
            result += data_column + delimiter
        if line == 0:
            content[-1] += '\n'
            content.append(result)
        else:
            content[line-1] = content[line-1].strip() +  result + '\n'
            # Write them back to the file
        with open(file_name, 'w') as f:
            f.writelines(content)