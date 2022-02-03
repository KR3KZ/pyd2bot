from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDuration(ObjectEffect):
    days:int
    hours:int
    minutes:int
    

    def init(self, days:int, hours:int, minutes:int, actionId:int):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        
        super().__init__(actionId)
    
    