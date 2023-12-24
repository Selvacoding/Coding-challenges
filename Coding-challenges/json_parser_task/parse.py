import re

def parse_json(json_str):
    pattern = r'"([^"]*)"\s*:\s*((true|false|null|"[^"]*"|-?\d+(\.\d+)?)|\{.*?\}|\[.*?\])\s*'
    matches = re.findall(pattern, json_str, re.DOTALL)

    result = {}
    if matches:
        for key, value, _, _ in matches:
            if value.startswith('{'):
                # if the value is a nested object, recursively parse it
                result[key] = parse_json(value)
            elif value.startswith('['):
                # if the value is a list, parse it as a list of strings excluding empty strings
                result[key] = [item.strip('"') for item in value[1:-1].split(',') if item.strip('"')]
            elif value.lower() == 'true':
                result[key] = True
            elif value.lower() == 'false':
                result[key] = False
            elif value.lower() == 'null':
                result[key] = None
            elif value.startswith('"') and value.endswith('"'):
                # handle string values
                result[key] = value[1:-1]
            elif '.' in value:
                # handle float values
                result[key] = float(value)
            else:
                # handle integer values
                result[key] = int(value)

    return result


# here I am just using one valid example 
json_string = '{"key": "value","key-n": 101,"key-o": {},"key-l": []}'
parsed_json = parse_json(json_string)
print(parsed_json)
