import json
import os
import sys


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def fill_values(tests, values_dict):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    values_data = read_json(values_path)
    tests_data = read_json(tests_path)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)

    write_json(report_path, tests_data)
