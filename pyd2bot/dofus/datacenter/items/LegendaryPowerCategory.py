                     
   class LegendaryPowerCategory(IDataCenter):
      
      MODULE:str = "LegendaryPowersCategories"
      
      logger = logging.getLogger("bot")
      
      idAccessors:IdAccessors = IdAccessors(getLegendaryPowerCategoryById,getLegendaryPowersCategories)
       
      
      id:int
      
      categoryName:str
      
      categoryOverridable:bool
      
      categorySpells:list[int]
      
      def __init__(self):
         super().__init__()
      
      def getLegendaryPowerCategoryById(self, id:int) -> LegendaryPowerCategory:
         return GameData.getObject(MODULE,id)
      
      def getLegendaryPowersCategories(self) -> list:
         return GameData.getObjects(MODULE)
