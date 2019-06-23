import yaml
import oyaml

class YamlIO:

    def read(self, file_name):
        f = open(file_name, "r")
        yaml_content = f.read()
        result = {}
        if('---' in yaml_content):
            seperate_yaml_files = yaml_content.split('---')
            result = []
            for yf in seperate_yaml_files:
                result.append(yaml.load(yf, Loader=yaml.FullLoader))
        else:
            result = yaml.load(yaml_content, Loader=yaml.FullLoader)
        f.close()
        return result

    def write(self, file_name, data):
        if type(data) is list:
            with open(file_name, 'w') as outfile:
                oyaml.dump_all(data, outfile, default_flow_style=False)
        elif type(data) is dict:
            with open(file_name, 'w') as outfile:
                oyaml.dump(data, outfile, default_flow_style=False)
