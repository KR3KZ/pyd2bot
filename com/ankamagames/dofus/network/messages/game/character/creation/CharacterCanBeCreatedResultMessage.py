from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterCanBeCreatedResultMessage(INetworkMessage):
    protocolId = 9527
    yesYouCan:bool
    
    
