from com.ankamagames.jerakine.logger.Logger import Logger
import re
logger = Logger(__name__)  


class StringUtils:


   def fill(str:str, len:int, char:str, before:bool = True) -> str:
      if not char or not len(char):
         return str
      while len(str) != len:
         if before:
            str = char + str
         else:
            str += char
      return str

   def concatSamestr(pstr:str, pstrToConcat:str) -> str:
      firstIndex:int = pstr.find(pstrToConcat)
      previousIndex:int = 0
      currentIndex:int = firstIndex
      while currentIndex != -1:
         previousIndex = currentIndex
         currentIndex = pstr.find(pstrToConcat, previousIndex + 1)
         if currentIndex == firstIndex:
            break
         if currentIndex == previousIndex + len(pstrToConcat):
            pstr = pstr[0:currentIndex]  + pstr[currentIndex + len(pstrToConcat):] 
            currentIndex -= len(pstrToConcat)
      return pstr


   def getDelimitedText(pText:str, pFirstDelimiter:str, pSecondDelimiter:str, pIncludeDelimiter:bool = False) -> list[str]:
      r = re.findall(re.escape(pFirstDelimiter) + r"(.*?)" + re.escape(pSecondDelimiter), pText)
      r = [_.lstrip(pFirstDelimiter).rstrip(pSecondDelimiter) for _ in r]
      if pIncludeDelimiter:
         r = [pFirstDelimiter + _ + pSecondDelimiter for _ in r]
      return r
