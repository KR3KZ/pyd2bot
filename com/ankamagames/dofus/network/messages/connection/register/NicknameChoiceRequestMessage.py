from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NicknameChoiceRequestMessage(NetworkMessage):
    protocolId = 3297
    nickname:str
    
