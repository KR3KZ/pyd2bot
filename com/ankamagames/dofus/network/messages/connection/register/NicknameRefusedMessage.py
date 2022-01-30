from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NicknameRefusedMessage(NetworkMessage):
    protocolId = 2705
    reason:int
    
