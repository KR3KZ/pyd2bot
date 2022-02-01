from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity


class StartupActionAddObject(NetworkMessage):
    uid:int
    title:str
    text:str
    descUrl:str
    pictureUrl:str
    items:list[ObjectItemInformationWithQuantity]
    
    
