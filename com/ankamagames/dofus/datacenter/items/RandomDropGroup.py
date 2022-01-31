         
   class RandomDropGroup(IDataCenter):
      
      MODULE:str = "RandomDropGroups"
       
      
      id:int
      
      name:str
      
      description:str
      
      randomDropItems:list[RandomDropItem]
      
      displayContent:bool
      
      displayChances:bool
      
      _groupWeight:int
      
      def __init__(self):
         super().__init__()
      
      def getRandomDropGroupById(self, id:int) -> RandomDropGroup:
         return GameData.getObject(MODULE,id)
      
      def getAllRandomDropGroup(self) -> list:
         return GameData.getObjects(MODULE)
      
      @property
      def groupWeight(self) -> int:
         item:RandomDropItem = None
         self._groupWeight = 0
         for item in self.randomDropItems:
            self._groupWeight += item.probability
         return self._groupWeight
