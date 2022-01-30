from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceCreationResultMessage(INetworkMessage):
    protocolId = 4954
    result:int
    
    
