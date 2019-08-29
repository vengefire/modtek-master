import json
import re
import tokenize

from util.string import remove_comments


def remove_extraneous_commas(string):
    string = re.sub(r",\s*}", "}", string)
    return re.sub(r",\s*]", "]", string)


def unescape_quotes(string):
    return string.replace(r"\'", r"'")


def delimit_consecutive_arrays(string):
    return re.sub(r"]\s*\[", '],[', string)


def delimit_consecutive_properties(string):
    # un-delimited consecutive objects
    string = re.sub(r"}\s*{", '},{', string)
    # un-delimited consecutive arrays
    string = re.sub(r"]\s*\"", '],"', string)
    # un-delimited consecutive quoted properties
    string = re.sub(r"\"\s*\"", '","', string)
    # un-delimited consecutive non-quoted properties
    string = re.sub(r"([^{},[:\s]$\s*)\"", "\g<1>,\"", string, flags=re.MULTILINE)
    return string


def load_json_from_file(path):
    with tokenize.open(path) as file:
        string = file.read()
        string = remove_comments(string)
        string = unescape_quotes(string)
        string = remove_extraneous_commas(string)
        string = delimit_consecutive_arrays(string)
        string = delimit_consecutive_properties(string)
        return json.loads(string)
