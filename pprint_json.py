import json


def load_data(filepath):
    with open(filepath) as f:
        json_data = json.load(f)
    return json_data


def pretty_print_json(data, key=None, offset=0, last=False):
    if type(data) == list:
        if key:
            print('"{}": {}'.format(key, '['))
        else:
            print('{}{}'.format("  "*offset, '['))
        data_len = len(data)
        for index, part in enumerate(data):
            if index == data_len-1:
                pretty_print_json(part, offset=offset+1, last=True)
            else:
                pretty_print_json(part, offset=offset+1)

        print('{}{}{}'.format("  "*offset, ']', '' if last else ','))
    elif type(data) == dict:
        if key:
            print('{}{}'.format('"'+key+'": ' if key else '', '{'))
        else:
            print('{}{}'.format("  "*offset, '{'))
        dict_len = len(data)
        for index, key in enumerate(sorted(data)):
            value = data[key]
            if index == dict_len-1:
                pretty_print_json((key, value), offset=offset+1, last=True)
            else:
                pretty_print_json((key, value), offset=offset+1)
        print('{}{}{}'.format("  "*offset, '}', '' if last else ','))
    elif type(data) == tuple:
        tkey, tvalue = data
        print("  "*offset, end='')
        if type(tvalue) in (str, bytes):
            print('"{}": "{}"{}'.format(data[0], data[1], '' if last else ','))
        elif type(tvalue) in (float, int):
            print('"{}": {}{}'.format(data[0], data[1], '' if last else ','))
        elif tvalue == None:
            print('"{}": "{}"{}'.format(data[0], 'null', '' if last else ','))
        else:
            pretty_print_json(tvalue, offset=offset, key=tkey)
    else:
        print("  "*offset, end='')
        print('{}{}'.format(data, '' if last else ','))

if __name__ == '__main__':

    json_data = load_data('alkoshops.json')
    pretty_print_json(json_data[:2])
