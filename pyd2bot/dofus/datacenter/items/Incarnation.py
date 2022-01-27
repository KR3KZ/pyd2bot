         
   class Incarnation(IDataCenter):
      
      MODULE:str = "Incarnation"
      
      _incarnationsList:list
       
      
      id:int
      
      maleBoneId:int
      
      femaleBoneId:int
      
      lookMale:str
      
      lookFemale:str
      
      def __init__(self):
         super().__init__()
      
      def getIncarnationById(self, id:int) -> Incarnation:
         return GameData.getObject(MODULE,id)
      
      def getAllIncarnation(self) -> list:
         if not _incarnationsList:
            _incarnationsList = GameData.getObjects(MODULE)
         return _incarnationsList
