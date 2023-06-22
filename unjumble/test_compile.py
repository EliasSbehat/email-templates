import json

version = "8-6-23"

# with open("19-05-email-example.json", "r") as f:
with open("data.json", "r") as f:
# with open("data.json", "r") as f:
    data = json.load(f)

from pybars import Compiler


with open(f'{version}.html', 'r') as f:
    template_source = f.read()
    compiler = Compiler()
    template = compiler.compile(template_source)
# pass the data and helper functions
compiled = template(data)

with open(f'{version}-compiled.html', 'w') as f:
    f.write(compiled)