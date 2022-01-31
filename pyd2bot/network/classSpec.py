from dataclasses import dataclass, field
from typing import List, Optional
import marshmallow_dataclass
import marshmallow.validate


@dataclass
class Field:
    name: str
    type: str
    dynamicType: bool
    typeId: int
    typename: str
    optional: bool
    length: int = None

@dataclass
class ClassSpec:
    name:str
    package:str
    parent:str
    protocolId:int
    fields:list[Field]
    boolfields:list[tuple[str, bool]]
    hash_function:str=None


if __name__ == "__main__":
    classSchema = marshmallow_dataclass.class_schema(ClassSpec)()
    r:ClassSpec = classSchema.load(spec)
    print(r.fields)