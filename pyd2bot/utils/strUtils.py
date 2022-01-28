

import re

def getDelimitedText(pText:str, pFirstDelimiter:str, pSecondDelimiter:str, pIncludeDelimiter:bool = False) -> list[str]:
    res = []
    while True:
        result = re.search(f"{pFirstDelimiter}(.*){pSecondDelimiter}", pText)
        if result:
            res.append(result.group(1))
            print(f"{pFirstDelimiter}{result.group(1)}{pSecondDelimiter}")
            res.remove(f"{pFirstDelimiter}{result.group(1)}{pSecondDelimiter}")
        else:
            break
    return res

def getAllIndexOf(c, searchstr):
    return [i for i, letter in enumerate(searchstr) if letter == c]
