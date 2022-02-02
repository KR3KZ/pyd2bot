from com.ankamagames.dofus.misc.BuildTypeParser import BuildTypeParser
from com.ankamagames.dofus.network.enums.BuildTypeEnum import BuildTypeEnum
from com.ankamagames.jerakine.types.Version import Version

class BuildInfos:
   
   VERSION:Version = Version("2.42.0", BuildTypeEnum.RELEASE)
   
   BUILD_DATE:str = "01/Jan/1970"
   
   
   def __init__(self):
      super().__init__()
   
   @property
   def buildTypeName(self) -> str:
      return BuildTypeParser.getTypeName(self.VERSION.buildType)
   
   @property
   def BUILD_TYPE(self) -> int:
      return self.VERSION.buildType
