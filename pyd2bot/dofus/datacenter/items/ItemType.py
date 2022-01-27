                        
   class ItemType(IDataCenter):
      
      MODULE:str = "ItemTypes"
      
      logger = logging.getLogger("bot")
      
      idAccessors:IdAccessors = IdAccessors(getItemTypeById,getItemTypes)
       
      
      _zoneSize:int = 4.294967295E9
      
      _zoneShape:int = 4.294967295E9
      
      _zoneMinSize:int = 4.294967295E9
      
      id:int
      
      nameId:int
      
      superTypeId:int
      
      categoryId:int
      
      isInEncyclopedia:bool
      
      plural:bool
      
      gender:int
      
      rawZone:str
      
      mimickable:bool
      
      craftXpRatio:int
      
      evolutiveTypeId:int
      
      _name:str
      
      _evolutiveType:EvolutiveItemType
      
      def __init__(self):
         super().__init__()
      
      def getItemTypeById(self, id:int) -> ItemType:
         return GameData.getObject(MODULE,id)
      
      def getItemTypes(self) -> list:
         return GameData.getObjects(MODULE)
      
      @property
      def name(self) -> str:
         if not self._name:
            self._name = I18n.getText(self.nameId)
         return self._name
      
      @property
      def evolutiveType(self) -> EvolutiveItemType:
         if not self._evolutiveType:
            if self.evolutiveTypeId == 0:
               return None
            self._evolutiveType = EvolutiveItemType.getEvolutiveItemTypeById(self.evolutiveTypeId)
         return self._evolutiveType
      
      @property
      def zoneSize(self) -> int:
         if self._zoneSize == int.MAX_VALUE:
            self.parseZone()
         return self._zoneSize
      
      @property
      def zoneShape(self) -> int:
         if self._zoneShape == int.MAX_VALUE:
            self.parseZone()
         return self._zoneShape
      
      @property
      def zoneMinSize(self) -> int:
         if self._zoneMinSize == int.MAX_VALUE:
            self.parseZone()
         return self._zoneMinSize
      
      def parseZone(self) -> None:
         params:list = None
         if self.rawZone and len(self.rawZone):
            self._zoneShape = self.rawZone.charCodeAt(0)
            params = self.rawZone.substr(1).split(",")
            if len(params) > 0:
               self._zoneSize = parseInt(params[0])
            else:
               self._zoneSize = 0
            if len(params) > 1:
               self._zoneMinSize = parseInt(params[1])
            else:
               self._zoneMinSize = 0
         else:
            logger.error("Zone incorrect (" + self.rawZone + ")")
