from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccountLoggingKickedMessage(NetworkMessage):
    protocolId = 7661
    days:int
    hours:int
    minutes:int
    
    
