from com.ankamagames.dofus.network.messages.game.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage


class GuildListApplicationRequestMessage(PaginationRequestAbstractMessage):
    

    def init(self, offset:int, count:int):
        
        super().__init__(offset, count)
    
    