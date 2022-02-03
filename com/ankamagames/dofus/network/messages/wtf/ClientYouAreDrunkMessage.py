from com.ankamagames.dofus.network.messages.debug.DebugInClientMessage import DebugInClientMessage


class ClientYouAreDrunkMessage(DebugInClientMessage):
    

    def init(self, level:int, message:str):
        
        super().__init__(level, message)
    
    