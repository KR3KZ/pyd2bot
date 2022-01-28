

from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.data.abstractDataManager import AbstractDataManager


class I18n(AbstractDataManager):
      
   
   def __init__(self):
      super().__init__()
   
   def addOverride(self, id:int, newId:int) -> None:
      I18nFileAccessor.getInstance().overrideId(id,newId)
   
   def getText(self, id:int, params:list = None, replace:str = "%") -> str:
      if not id:
         return None
      txt:str = I18nFileAccessor.getInstance().getText(id)
      if txt == None or txt == "None":
         return "[UNKNOWN_TEXT_ID_" + id + "]"
      return I18n.replaceParams(txt,params,replace)
   
   def getUnDiacriticalText(self, id:int, params:list = None, replace:str = "%") -> str:
      if not id:
         return None
      txt:str = I18nFileAccessor.getInstance().getUnDiacriticalText(id)
      if txt == None or txt == "None":
         return "[UNKNOWN_TEXT_ID_" + id + "]"
      return I18n.replaceParams(txt,params,replace)
   
   def getUiText(self, textId:str, params:list = None, replace:str = "%") -> str:
      txt:str = I18nFileAccessor.getInstance().getNamedText(textId)
      if txt == None or txt == "None":
         return "[UNKNOWN_TEXT_NAME_" + textId + "]"
      return self.replaceParams(txt,params,replace)
   
   def hasUiText(self, textId:str) -> bool:
      return I18nFileAccessor.getInstance().hasNamedText(textId)
   
   @staticmethod
   def replaceParams(text:str, params:list, replace:str) -> str:
      if not params or len(not params):
         return text
      for i in range(1, len(params), 1):
         text = text.replace(replace + i,params[i - 1])
      return text
