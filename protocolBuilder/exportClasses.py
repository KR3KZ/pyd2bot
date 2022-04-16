import importlib
import os
from pathlib import Path
import sys
from tkinter import N
from jinja2 import Template
import json
from tqdm import tqdm
import com.ankamagames.dofus.Constants as Constants

PRIMITIVES = ["int", "float", "bool", "str", "list", "dict", "bytearray"]
ROOTDIR = Path(os.path.dirname(__file__))
with open(Constants.PROTOCOL_SPEC_PATH, "r") as fp:
    json_spec = json.load(fp)


def getInitArgs(spec):
    init_args = []
    nonPrimitives = []
    for field in spec["fields"]:
        if field["typename"] in PRIMITIVES:
            typename = field["typename"]
        else:
            typename = f"'{field['typename']}'"
            nonPrimitives.append(field["typename"])
        ftype = (
            typename
            if field["length"] is None and field["lengthTypeId"] is None
            else "list[" + typename + "]"
        )
        init_args.append({"name": field["name"], "type": ftype})
    for field in spec["boolfields"]:
        init_args.append({"name": field["name"], "type": field["typename"]})
    return init_args, nonPrimitives


def main():
    with open(ROOTDIR / "template.j2", "r") as f:
        template = Template(f.read())
        for name, msg in tqdm(json_spec["type"].items()):
            init_args, nonPrimitives = getInitArgs(msg)

            super_args = []
            current = msg.get("parent")
            while current:
                current = json_spec["type"][current]
                inArgs, nonPrim = getInitArgs(current)
                nonPrimitives.extend(nonPrim)
                super_args.extend(inArgs)
                current = current.get("parent")

            r = template.render(
                cls=msg,
                types=json_spec["type"],
                super_args=super_args,
                init_args=init_args,
                nonPrimitives=nonPrimitives,
                primitives=PRIMITIVES,
            )

            path_to = msg["package"].replace(".", "/")
            path_to = "{}.py".format(path_to)
            if not os.path.exists(Path(path_to).parent):
                os.makedirs(Path(path_to).parent)
            with open(path_to, "w") as f:
                f.write(r)


if __name__ == "__main__":
    main()
