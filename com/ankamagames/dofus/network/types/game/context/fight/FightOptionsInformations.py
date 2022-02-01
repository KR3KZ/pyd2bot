from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FightOptionsInformations(INetworkMessage):
    protocolId = 5639
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    
    
