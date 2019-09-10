import jsonschema
import yaml

schema_file = 'C:\DATA_\Reading Material\git_repos\examples\python\Programs\jsonschema\schema_testsuite.json'
testsuite_file = r'C:\DATA_\Reading Material\git_repos\examples\python\Programs\jsonschema\testsuite_file.yaml'

def _load_yaml(file_name=None):
    if (file_name is None):
        raise Exception("Missing required parameter 'file_name'")
    import yaml
    with open(file_name, 'r') as file_h:
        return yaml.load(file_h, Loader=yaml.FullLoader)

def _load_json(file_name=None):
    if (file_name is None):
        raise Exception("Missing required parameter 'file_name'")
    import json
    with open(file_name, 'r') as file_h:
        return json.load(file_h)

def load_schema_file():
    return _load_json(file_name = schema_file)

def load_yaml_file():
    return _load_yaml(file_name = testsuite_file)

def validate():
    schema = load_schema_file()
    testsuite_yaml = load_yaml_file()

    jsonschema.validate(testsuite_yaml, schema)
    return testsuite_yaml

def main():
    try:
        res = validate()
        print("res:\n")
        print(res)
    except Exception as ex:
        print("Error: " + str(ex))

if __name__ == '__main__':
    main()
