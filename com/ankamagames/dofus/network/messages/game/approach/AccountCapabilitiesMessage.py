from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccountCapabilitiesMessage(INetworkMessage):
    protocolId = 8644
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    
    
