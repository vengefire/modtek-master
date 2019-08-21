import json
import re
import tokenize

from util.string import remove_comments


def remove_extraneous_commas(string):
    string = re.sub(r",\s*}", "}", string)
    string = re.sub(r",\s*]", "]", string)
    return string


def load_json_from_file(path):
    with tokenize.open(path) as file:
        string = file.read()
        string = remove_comments(string)
        string = remove_extraneous_commas(string)
        return json.loads(string)
