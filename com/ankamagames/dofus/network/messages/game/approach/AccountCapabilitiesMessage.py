from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    
    
