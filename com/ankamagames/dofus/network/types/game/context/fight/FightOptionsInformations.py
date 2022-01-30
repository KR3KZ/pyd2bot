from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FightOptionsInformations(INetworkMessage):
    protocolId = 5639
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    
    
