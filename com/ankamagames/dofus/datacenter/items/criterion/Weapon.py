         
   class Weapon(Item implements IDataCenter):
      
      idAccessors:IdAccessors = IdAccessors(getWeaponById,getWeapons)
       
      
      apCost:int
      
      minRange:int
      
      range:int
      
      maxCastPerTurn:int
      
      castInLine:bool
      
      castInDiagonal:bool
      
      castTestLos:bool
      
      criticalHitProbability:int
      
      criticalHitBonus:int
      
      criticalFailureProbability:int
      
      def __init__(self):
         super().__init__()
      
      def getWeaponById(self, weaponId:int) -> Weapon:
         item:Item = Item.getItemById(weaponId)
         if item and item.isWeapon:
            return Weapon(item)
         return None
      
      def getWeapons(self) -> list:
         item:Item = None
         items:list = Item.getItems()
         result:list = list()
         for item in items:
            if item.isWeapon:
               result.append(item)
         return result
      
      @property
      def isWeapon(self) -> bool:
         return True
      
      def copy(self, from:Item, to:Item) -> None:
         super().copy(from,to)
         if to.hasOwnProperty("apCost") and from.hasOwnProperty("apCost"):
            Object(to).apCost = Object(from).apCost
            Object(to).minRange = Object(from).minRange
            Object(to).range = Object(from).range
            Object(to).maxCastPerTurn = Object(from).maxCastPerTurn
            Object(to).castInLine = Object(from).castInLine
            Object(to).castInDiagonal = Object(from).castInDiagonal
            Object(to).castTestLos = Object(from).castTestLos
            Object(to).criticalHitProbability = Object(from).criticalHitProbability
            Object(to).criticalHitBonus = Object(from).criticalHitBonus
            Object(to).criticalFailureProbability = Object(from).criticalFailureProbability
         else:
            logger.error("Failed to properly copy weapon data " + from.id + " to " + to.id)
