import json

class JsonIO:

    def read(self, file_name):
        f = open(file_name, "r")
        result = f.read()
        f.close()
        return json.loads(result)

    def write(self, file_name, data):
        with open(file_name, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)