import importlib
import sys
from jinja2 import Template
import json

msg = r"""{
            "name": "GameActionMark",
            "rpath": "game\\actions\\fight\\GameActionMark.as",
            "parent": null,
            "protocolId": 158,
            "vars": [
                {
                    "name": "markAuthorId",
                    "length": null,
                    "type": "Double",
                    "pytype": "float",
                    "optional": false
                },
                {
                    "name": "markTeamId",
                    "length": null,
                    "type": "Byte",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "markSpellId",
                    "length": null,
                    "type": "Int",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "markSpellLevel",
                    "length": null,
                    "type": "Short",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "markId",
                    "length": null,
                    "type": "Short",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "markType",
                    "length": null,
                    "type": "Byte",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "markimpactCell",
                    "length": null,
                    "type": "Short",
                    "pytype": "int",
                    "optional": false
                },
                {
                    "name": "cells",
                    "length": "Short",
                    "type": "GameActionMarkedCell",
                    "optional": false
                },
                {
                    "name": "active",
                    "length": null,
                    "type": "Boolean",
                    "optional": false
                }
            ],
            "boolVars": [],
            "hash_function": false
}"""
msg_dict = json.loads(msg)


# def convertToClassInstance(self, jsonObj):
#     moduleName = jsonObj["package"]
#     try:
#         module = sys.modules[moduleName]
#     except:
#         module = importlib.import_module(moduleName)
#     cls = getattr(module, jsonObj["name"])
#     for field in jsonObj["fields"]:
#         if field["legth"] is None:

with open("protocolBuilder/template.j2", "r") as f:
    template = Template(f.read())
    r = template.render(msg=msg_dict)
    print(r)