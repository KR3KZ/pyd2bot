from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NicknameRefusedMessage(INetworkMessage):
    protocolId = 2705
    reason:int
    
    
