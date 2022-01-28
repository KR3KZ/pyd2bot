                     
   class EvolutiveItemType(IDataCenter):
      
      MODULE:str = "EvolutiveItemTypes"
      
      logger = logging.getLogger("bot")
      
      idAccessors:IdAccessors = IdAccessors(getEvolutiveItemTypeById,getEvolutiveItemTypes)
       
      
      id:int
      
      maxLevel:int
      
      experienceBoost:float
      
      experienceByLevel:list[int]
      
      def __init__(self):
         super().__init__()
      
      def getEvolutiveItemTypeById(self, id:int) -> EvolutiveItemType:
         return GameData.getObject(MODULE,id)
      
      def getEvolutiveItemTypes(self) -> list:
         return GameData.getObjects(MODULE)
      
      def getLevelFromExperiencePoints(self, experience:int) -> int:
         for i:int = 1 i <= self.maxLevel :
            if self.experienceByLevel[i] > experience:
               break
            i += 1
         return i - 1
      
      def getMaxExperienceForLevel(self, level:int) -> int:
         experienceForNextLevel:int = self.experienceByLevel[level + 1]
         return experienceForNextLevel - 1
