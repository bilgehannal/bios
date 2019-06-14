
class StandartIO:

    def read(self, file_name):
        f = open(file_name, "r")
        result = f.read()
        f.close()
        return result

    def write(self, file_name, data):
        f = open(file_name, "w")
        f.write(data)
        f.close()

    def append(self, file_name, data, line):
        content = ''
        with open(file_name, 'r') as f:
            content = f.readlines()
        if line == 0:
            content[-1] += '\n'
            content.append(data)
        else:
            content[line-1] = content[line-1].strip() +  data + '\n'
            # Write them back to the file
        with open(file_name, 'w') as f:
            f.writelines(content)