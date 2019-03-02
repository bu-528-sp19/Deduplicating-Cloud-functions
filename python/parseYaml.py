import sys
from ruamel.yaml import YAML

def parse_yaml():
    inp = """\
    # example
    bucket:
      # details
      input: input
      output: outout
    function:
      path: "thumbnail.py"
    """

    yaml = YAML()
    code = yaml.load(inp)
    fileName = (code['function']['path'])

    return fileName

#yaml.dump(code, sys.stdout)

if __name__ == "__main__":
    parse_yaml()