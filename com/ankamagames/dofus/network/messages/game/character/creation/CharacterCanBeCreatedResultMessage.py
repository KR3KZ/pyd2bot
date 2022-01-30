from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterCanBeCreatedResultMessage(NetworkMessage):
    protocolId = 9527
    yesYouCan:bool
    
