from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity


class StartupActionAddObject(NetworkMessage):
    protocolId = 6157
    uid:int
    title:str
    text:str
    descUrl:str
    pictureUrl:str
    items:ObjectItemInformationWithQuantity
    
