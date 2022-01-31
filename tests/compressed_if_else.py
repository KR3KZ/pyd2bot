import re


stat = '\n         var smonth:String = this.month > 9 ? String(this.month) : "0" + String(this.month);'


def processCompressedIfELse(line):
    m = re.fullmatch("(?P<leftSide>[^=]* = )(?P<content>.*)", line)
    if m:
        leftSide = m.group("leftSide")
        content = m.group("content")
    else:
        content = line
        leftSide = ""
    i = content.find("?")
    if i == -1:
        return line
    else:
        j = content.rfind(":")
        return leftSide + processCompressedIfELse(content[i+1:j]) + "if " + content[:i] + "else" + content[j+1:]

def processCompressedIfELseInAllCode(code):
    codeLines = code.split("\n")
    regex = r"(.*) ? (.*) : (.*)"
    r = []
    for line in codeLines:
        m = re.match(regex, line)
        if m:
            r.append(processCompressedIfELse(line))
        else:
            r.append(line)
    return "\n".join(r)

print(processCompressedIfELseInAllCode(stat))
