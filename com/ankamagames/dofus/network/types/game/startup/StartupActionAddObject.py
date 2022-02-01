from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity


class StartupActionAddObject(INetworkMessage):
    protocolId = 6157
    uid:int
    title:str
    text:str
    descUrl:str
    pictureUrl:str
    items:ObjectItemInformationWithQuantity
    
    
