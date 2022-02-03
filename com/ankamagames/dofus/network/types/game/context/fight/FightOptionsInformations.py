from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightOptionsInformations(NetworkMessage):
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    

    def init(self):
        
        super().__init__()
    
    