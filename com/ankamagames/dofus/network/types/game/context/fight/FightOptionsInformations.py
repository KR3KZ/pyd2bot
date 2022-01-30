from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FightOptionsInformations(NetworkMessage):
    protocolId = 5639
    isSecret:bool
    isRestrictedToPartyOnly:bool
    isClosed:bool
    isAskingForHelp:bool
    
    
