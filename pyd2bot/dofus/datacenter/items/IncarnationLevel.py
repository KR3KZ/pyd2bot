         
   class IncarnationLevel(IDataCenter):
      
      MODULE:str = "IncarnationLevels"
       
      
      id:int
      
      incarnationId:int
      
      level:int
      
      requiredXp:int
      
      def __init__(self):
         super().__init__()
      
      def getIncarnationLevelById(self, id:int) -> IncarnationLevel:
         return GameData.getObject(MODULE,id)
      
      def getIncarnationLevelByIdAndLevel(self, incarnationId:int, level:int) -> IncarnationLevel:
         id:int = incarnationId * 100 + level
         return getIncarnationLevelById(id)
      
      @property
      def incarnation(self) -> Incarnation:
         return Incarnation.getIncarnationById(self.id)
