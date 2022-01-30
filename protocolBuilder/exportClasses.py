import importlib
import os
from pathlib import Path
import sys
from jinja2 import Template
import json
from tqdm import tqdm


with open("protocolBuilder/spec.json", 'r') as fp:
    json_spec = json.load(fp)

with open("protocolBuilder/template.j2", "r") as f:
    template = Template(f.read())
    for name, msg in tqdm(json_spec["type"].items()):
        r = template.render(cls=msg, types=json_spec["type"], primitives=["int", "float", "bool", "str", "list", "dict", "bytearray"])
        path_to = msg["package"].replace(".", "/")
        path_to = "{}.py".format(path_to)
        if not os.path.exists(Path(path_to).parent):
            os.makedirs(Path(path_to).parent)
        with open(path_to, "w") as f:
            f.write(r)