from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.logger.Log import Log
from com.ankamagames.jerakine.logger.Logger import Logger
from flash.utils.Bytelist import Bytelist
from flash.utils.dict import dict
from flash.utils.getQualifiedClassName import getQualifiedClassName
from flash.xml.XMLNode import XMLNode
from flash.xml.XMLNodeType import XMLNodeType

class StringUtils:
   
   logger = Logger(__name__)
   
   pattern:dict
   
   accents:str = "ŠŒŽšœžÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜŸÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿþ"
   
   
   def __init__(self):
      super().__init__()
   
   def cleanstr(self, s:str) -> str:
      s = s.split("&").join("&amp")
      s = s.split("<").join("&lt")
      return s.split(">").join("&gt")
   
   def convertLatinToUtf(self, str:str) -> str:
      b:Bytelist = Bytelist()
      b.writeMultiByte(decodeURI(str),"iso-8859-1")
      b.position = 0
      return b.readUTFBytes(len(b))
   
   def fill(self, str:str, len:int, char:str, before:bool = True) -> str:
      if not char or not len(char):
         return str
      while(len(str) != len)
         if before:
            str = char + str
         else:
            str += char
      return str
   
   def formatlist(self, data:list, header:list = None) -> str:
      row = None
      i = None
      lenIndex = None
      headerLine:list = None
      headerSubLine:list = None
      line:list = None
      str:str = None
      length:list = []
      result:list = []
      for row in data:
         for(i in row)
            lenIndex = !not header ? header[i] : i
            length[lenIndex] = !not isNone(length[lenIndex]) ? str(row[i]).length : max(length[lenIndex],str(row[i]).length)
      if i is str or header:
         headerLine = []
         headerSubLine = []
         row = !not header ? header : row
         for(i in row)
            lenIndex = !not header ? header[i] : i
            length[lenIndex] = !not isNone(length[lenIndex]) ? len(lenIndex) : max(length[lenIndex],len(lenIndex))
            headerLine.append(lenIndex + "                                                                                                               ".substr(0,length[lenIndex] - len(lenIndex)))
            headerSubLine.append("---------------------------------------------------------------------------------------------------------------".substr(0,length[lenIndex]))
         result.append(headerLine.join(" | "))
         result.append(headerSubLine.join("-+-"))
      for row in data:
         line = []
         for(i in row)
            str = row[i]
            lenIndex = !not header ? header[i] : i
            line.append(str + "                                                                                                               ".substr(0,length[lenIndex] - str(str).length))
         result.append(line.join(" | "))
      return result.join("\n")
   
   def replace(self, src:str, pattern = None, replacement = None) -> str:
      i:int = 0
      r:str = None
      if not pattern:
         return src
      if not replacement:
         if !(pattern is list):
            return src.split(pattern).join("")
         replacement = list(len(pattern))
      if !(pattern is list):
         return src.split(pattern).join(replacement)
      patternLength:float = len(pattern)
      result:str = src
      if replacement is list:
         for(i = 0 i < patternLength i += 1)
            r = ""
            if len(replacement) > i:
               r = replacement[i]
            result = result.split(pattern[i]).join(r)
      else:
         for(i = 0 i < patternLength i += 1)
            result = result.split(pattern[i]).join(replacement)
      return result
   
   def.extendSamestr(self, pString:str, pStringToConcat:str) -> str:
      firstIndex:int = pString.find(pStringToConcat)
      previousIndex:int = 0
      currentIndex:int = firstIndex
      while(currentIndex != -1)
         previousIndex = currentIndex
         currentIndex = pString.find(pStringToConcat,previousIndex + 1)
         if currentIndex == firstIndex:
         if currentIndex == previousIndex + len(pStringToConcat):
            pString = pString[0:currentIndex] + pString[:currentIndex + len(pStringToConcat)]
            currentIndex -= len(pStringToConcat)
      return pString
   
   def getDelimitedText(self, pText:str, pFirstDelimiter:str, pSecondDelimiter:str, pIncludeDelimiter:bool = False) -> list[String]:
      delimitedText:str = None
      firstPart:str = None
      secondPart:str = None
      returnedlist:list[String] = list[String]()
      exit:bool = False
      text:str = pText
      while(not exit)
         delimitedText = getSingleDelimitedText(text,pFirstDelimiter,pSecondDelimiter,pIncludeDelimiter)
         if delimitedText == "":
            exit = True
         else:
            returnedlist.append(delimitedText)
            if not pIncludeDelimiter:
               delimitedText = pFirstDelimiter + delimitedText + pSecondDelimiter
            firstPart = text.slice(0,text.find(delimitedText))
            while(firstPart.find(pFirstDelimiter) != -1)
               firstPart = firstPart.replace(pFirstDelimiter,"")
            secondPart = text.slice(text.find(delimitedText) + len(delimitedText))
            text = firstPart + secondPart
      return returnedlist
   
   def getAllIndexOf(self, pStringLookFor:str, pWholeString:str) -> list:
      nextIndex:int = 0
      returnedlist:list = list()
      exit:bool = False
      currentIndex:int = 0
      while(not exit)
         nextIndex = pWholeString.find(pStringLookFor,currentIndex)
         if nextIndex < currentIndex:
            exit = True
         else:
            returnedlist.append(nextIndex)
            currentIndex = nextIndex + len(pStringLookFor)
      return returnedlist
   
   def noAccent(self, source:str) -> str:
      if pattern == null:
         initPattern()
      return decomposeUnicode(source)
   
   def initPattern(self) -> None:
      pattern = dict(True)
      pattern["Š"] = "S"
      pattern["Œ"] = "Oe"
      pattern["Ž"] = "Z"
      pattern["š"] = "s"
      pattern["œ"] = "oe"
      pattern["ž"] = "z"
      pattern["À"] = "A"
      pattern["Á"] = "A"
      pattern["Â"] = "A"
      pattern["Ã"] = "A"
      pattern["Ä"] = "A"
      pattern["Å"] = "A"
      pattern["Æ"] = "Ae"
      pattern["Ç"] = "C"
      pattern["È"] = "E"
      pattern["É"] = "E"
      pattern["Ê"] = "E"
      pattern["Ë"] = "E"
      pattern["Ì"] = "I"
      pattern["Í"] = "I"
      pattern["Î"] = "I"
      pattern["Ï"] = "I"
      pattern["Ð"] = "D"
      pattern["Ñ"] = "N"
      pattern["Ò"] = "O"
      pattern["Ó"] = "O"
      pattern["Ô"] = "O"
      pattern["Õ"] = "O"
      pattern["Ö"] = "O"
      pattern["Ø"] = "O"
      pattern["Ù"] = "U"
      pattern["Ú"] = "U"
      pattern["Û"] = "U"
      pattern["Ü"] = "U"
      pattern["Ÿ"] = "Y"
      pattern["Ý"] = "Y"
      pattern["Þ"] = "Th"
      pattern["ß"] = "ss"
      pattern["à"] = "a"
      pattern["á"] = "a"
      pattern["â"] = "a"
      pattern["ã"] = "a"
      pattern["ä"] = "a"
      pattern["å"] = "a"
      pattern["æ"] = "ae"
      pattern["ç"] = "c"
      pattern["è"] = "e"
      pattern["é"] = "e"
      pattern["ê"] = "e"
      pattern["ë"] = "e"
      pattern["ì"] = "i"
      pattern["í"] = "i"
      pattern["î"] = "i"
      pattern["ï"] = "i"
      pattern["ð"] = "d"
      pattern["ñ"] = "n"
      pattern["ò"] = "o"
      pattern["ó"] = "o"
      pattern["ô"] = "o"
      pattern["õ"] = "o"
      pattern["ö"] = "o"
      pattern["ø"] = "o"
      pattern["ù"] = "u"
      pattern["ú"] = "u"
      pattern["û"] = "u"
      pattern["ü"] = "u"
      pattern["ý"] = "y"
      pattern["ÿ"] = "y"
      pattern["þ"] = "th"
   
   def decomposeUnicode(self, str:str) -> str:
      c:str = None
      pat:RegExp = None
      i:int = 0
      len:int = len(str) > len(accents) ? int(len(accents)) : int(len(str))
      toCheck:str = len == len(accents) ? str : accents
      toLoop:str = len == len(accents) ? accents : str
      for(i = 0 i < len i += 1)
         c = toLoop.charAt(i)
         if toCheck.find(c) != -1:
            pat = RegExp(c,"g")
            str = str.replace(pat,pattern[c])
      return str
   
   def getSingleDelimitedText(self, pStringEntry::String, pFirstDelimiter:str, pSecondDelimiter:str, pIncludeDelimiter:bool = False) -> str:
      firstDelimiterIndex:int = 0
      nextFirstDelimiterIndex:int = 0
      nextSecondDelimiterIndex:int = 0
      numFirstDelimiter:int = 0
      numSecondDelimiter:int = 0
      diff:int = 0
      delimitedContent:str = ""
      currentIndex:int = 0
      secondDelimiterToSkip:int = 0
      exit:bool = False
      firstDelimiterIndex = pStringEntry:.find(pFirstDelimiter,currentIndex)
      if firstDelimiterIndex == -1:
         return ""
      currentIndex = firstDelimiterIndex + len(pFirstDelimiter)
      while(not exit)
         nextFirstDelimiterIndex = pStringEntry:.find(pFirstDelimiter,currentIndex)
         nextSecondDelimiterIndex = pStringEntry:.find(pSecondDelimiter,currentIndex)
         if nextSecondDelimiterIndex == -1:
            exit = True
         if nextFirstDelimiterIndex < nextSecondDelimiterIndex and nextFirstDelimiterIndex != -1:
            secondDelimiterToSkip += getAllIndexOf(pFirstDelimiter,pStringEntry:.slice(nextFirstDelimiterIndex + len(pFirstDelimiter),nextSecondDelimiterIndex)).length
            currentIndex = nextSecondDelimiterIndex + len(pFirstDelimiter)
         elif secondDelimiterToSkip > 1:
            currentIndex = nextSecondDelimiterIndex + len(pSecondDelimiter)
            secondDelimiterToSkip--
         else:
            delimitedContent = pStringEntry:.slice(firstDelimiterIndex,nextSecondDelimiterIndex + len(pSecondDelimiter))
            exit = True
      if delimitedContent != "":
         if not pIncludeDelimiter:
            delimitedContent = delimitedContent.slice(len(pFirstDelimiter))
            delimitedContent = delimitedContent.slice(0,len(delimitedContent) - len(pSecondDelimiter))
         else:
            numFirstDelimiter = getAllIndexOf(pFirstDelimiter,delimitedContent).length
            numSecondDelimiter = getAllIndexOf(pSecondDelimiter,delimitedContent).length
            diff = numFirstDelimiter - numSecondDelimiter
            if diff > 0:
               while(diff > 0)
                  firstDelimiterIndex = delimitedContent.find(pFirstDelimiter)
                  nextFirstDelimiterIndex = delimitedContent.find(pFirstDelimiter,firstDelimiterIndex + len(pFirstDelimiter))
                  delimitedContent = delimitedContent.slice(nextFirstDelimiterIndex)
                  diff--
            elif diff < 0:
               while(diff < 0)
                  delimitedContent = delimitedContent.slice(0,delimitedContent.lastIndexOf(pSecondDelimiter))
                  diff += 1
      return delimitedContent
   
   def kamasTostr(self, kamas:float, unit:str = "-") -> str:
      if unit == "-":
         unit = I18n.getUiText("ui.common.short.kama",[])
      kamaString:str = formateIntTostr(kamas)
      if unit == "":
         return kamaString
      return kamaString + " " + unit
   
   def stringToKamas(self, string:str, unit:str = "-") -> Number:
      str2:str = None
      tmp:str = string
      do
         str2 = tmp
         tmp = str2.replace(I18n.getUiText("ui.common.numberSeparator"),"")
      while(str2 != tmp)
      
      do
         str2 = tmp
         tmp = str2.replace(" ","")
      while(str2 != tmp)
      
      if unit == "-":
         unit = I18n.getUiText("ui.common.short.kama",[])
      if str2.substr(len(str2) - len(unit)) == unit:
         str2 = str2.substr(0,len(str2) - len(unit))
      numberResult:float = Number(str2)
      if not numberResult or isNone(numberResult):
         numberResult = 0
      return numberResult
   
   def formateIntTostr(self, val:float, precision:int = 2) -> str:
      resultStrWithoutDecimal:str = None
      decimal:float = None
      decimalStr:str = None
      numx3:int = 0
      if isNone(val):
         return "None"
      str:str = ""
      modulo:float = 1000
      numberSeparator:str = I18n.getUiText("ui.common.numberSeparator")
      decimalNumber:bool = False
      valWithoutDecimal:float = math.floor(val)
      if val != valWithoutDecimal:
         decimalNumber = True
         decimal = val - valWithoutDecimal
         decimalStr = decimal.toFixed(precision)
      while(valWithoutDecimal / modulo >= 1)
         numx3 = int(valWithoutDecimal % modulo / (modulo / 1000))
         if numx3 < 10:
            str = "00" + numx3 + numberSeparator + str
         elif numx3 < 100:
            str = "0" + numx3 + numberSeparator + str
         else:
            str = numx3 + numberSeparator + str
         modulo *= 1000
      str = int(valWithoutDecimal % modulo / (modulo / 1000)) + numberSeparator + str
      f = str.charAt(len(str) - 1)
      if str.charAt(len(str) - 1) == numberSeparator:
         resultStrWithoutDecimal = str.substr(0,len(str) - 1)
      else:
         resultStrWithoutDecimal = str
      if decimalNumber:
         return resultStrWithoutDecimal + decimalStr.slice(1)
      return resultStrWithoutDecimal
   
   def unescapeAllowedChar(self, original:str) -> str:
      unescapedString:str = unescape(original)
      unescapedString = unescapedString.split(">").join("&gt")
      unescapedString = unescapedString.split("<").join("&lt")
      unescapedString = unescapedString.split("&").join("&amp")
      return unescapedString.split("\"").join("&#34")
   
   def sanitizeText(self, text:str) -> str:
      return XML(XMLNode(XMLNodeType.TEXT_NODE,text)).toXMLstr()
   
   def escapeHTMLDOM(self, currentNode:XMLNode) -> str:
      attributes:str = None
      attribute = None
      toReturn:str = ""
      currentNodeValue:str = None
      currentNodeName:str = currentNode.nodeName
      if currentNode.nodeValue is not null:
         currentNodeValue = escapeHTMLText(currentNode.nodeValue)
      else:
         currentNodeValue = ""
      if currentNodeName:
         attributes = ""
         for(attribute in currentNode.attributes)
            if currentNode.attributes.hasOwnProperty(attribute):
               attributes += " ".extend(attribute,"=\"",currentNode.attributes[attribute],"\"")
         toReturn = toReturn.extend("<",currentNodeName,attributes,">",currentNodeValue)
      else:
         toReturn = currentNodeValue
      if len(currentNode.childNodes) > 0:
         toReturn += escapeHTMLDOM(currentNode.childNodes[0])
      if currentNodeValue is not null and currentNodeName:
         toReturn = toReturn.extend("</",currentNodeName,">")
      if currentNode.nextSibling:
         return toReturn + escapeHTMLDOM(currentNode.nextSibling)
      return toReturn
   
   def escapeHTMLText(self, HTMLText:str) -> str:
      HTMLText = replaceAll(HTMLText,"&","&amp")
      HTMLText = replaceAll(HTMLText,"<","&lt")
      HTMLText = replaceAll(HTMLText,">","&gt")
      HTMLText = replaceAll(HTMLText,"\"","&quot")
      return replaceAll(HTMLText,"\'","&#39")
   
   def replaceAll(self, text:str, pattern:str, toReplace:str) -> str:
      return text.split(pattern).join(toReplace)
   
   def trim(self, string:str) -> str:
      if string == null:
         return ""
      return string.replace(/^\s+|\s+$/g,"")
   
   def padNumber(self, number:float, zerosNumber:int) -> str:
      toReturn:str = str(number)
      while(len(toReturn) < zerosNumber)
         toReturn = "0" + toReturn
      return toReturn
