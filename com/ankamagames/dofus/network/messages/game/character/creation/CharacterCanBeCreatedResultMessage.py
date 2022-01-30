from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterCanBeCreatedResultMessage(INetworkMessage):
    protocolId = 9527
    yesYouCan:bool
    
    
