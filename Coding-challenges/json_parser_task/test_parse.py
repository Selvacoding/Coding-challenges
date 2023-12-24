from parse import parse_json

def test_parse_1():
    json_string  = '{}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {}

def test_parse_2():
    json_string  = '{"key": "value"}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {"key": "value"}

def test_parse_3():
    json_string  = '{"key": "value","key2": "value"}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {"key": "value","key2": "value"}

def test_parse_4():
    json_string  = '{"key1": true,"key2": false,"key3": null,"key4": "value","key5": 101}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {"key1": True,"key2": False,"key3": None,"key4": "value","key5": 101}

def test_parse_5():
    json_string  = '{"key": "value","key-n": 101,"key-o": {},"key-l": []}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {"key": "value","key-n": 101,"key-o": {},"key-l": []}

def test_parse_6():
    json_string = '{"key": "value","key-n": 101,"key-o": {"inner key": "inner value"},"key-l": ["list value"]}'
    parsed_data = parse_json(json_string)
    assert parsed_data == {"key": "value","key-n": 101,"key-o": {"inner key": "inner value"},"key-l": ["list value"]}
