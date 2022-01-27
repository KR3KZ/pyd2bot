         
   class PresetIcon(IDataCenter):
      
      MODULE:str = "PresetIcons"
       
      
      id:int
      
      order:int
      
      def __init__(self):
         super().__init__()
      
      def getPresetIconById(self, id:int) -> PresetIcon:
         return GameData.getObject(MODULE,id)
      
      def getPresetIcons(self) -> list:
         return GameData.getObjects(MODULE)
