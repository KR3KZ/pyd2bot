from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDate(ObjectEffect):
    year:int
    month:int
    day:int
    hour:int
    minute:int
    

    def init(self, year:int, month:int, day:int, hour:int, minute:int, actionId:int):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        
        super().__init__(actionId)
    
    