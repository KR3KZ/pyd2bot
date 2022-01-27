                  
   class ItemSet(IDataCenter):
      
      MODULE:str = "ItemSets"
      
      idAccessors:IdAccessors = IdAccessors(getItemSetById,getItemSets)
       
      
      id:int
      
      items:list[int]
      
      nameId:int
      
      effects:list[Vector.<EffectInstance>]
      
      bonusIsSecret:bool
      
      _name:str
      
      def __init__(self):
         super().__init__()
      
      def getItemSetById(self, id:int) -> ItemSet:
         return GameData.getObject(MODULE,id)
      
      def getItemSets(self) -> list:
         return GameData.getObjects(MODULE)
      
      @property
      def name(self) -> str:
         if not self._name:
            self._name = I18n.getText(self.nameId)
         return self._name
