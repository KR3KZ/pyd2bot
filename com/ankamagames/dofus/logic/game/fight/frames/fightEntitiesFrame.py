

from com.ankamagames.dofus.logic.frames.IFrame import IFrame


class FightEntitiesFrame(IFrame):

    def __init__(self, bot):
        super().__init__(bot)
    
    def getEntityInfos(self, entityId:int) -> dict:
        return self.bot.currMap.entities[entityId]