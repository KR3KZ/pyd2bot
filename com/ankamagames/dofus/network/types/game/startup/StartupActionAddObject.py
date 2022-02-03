from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
    


class StartupActionAddObject(NetworkMessage):
    uid:int
    title:str
    text:str
    descUrl:str
    pictureUrl:str
    items:list['ObjectItemInformationWithQuantity']
    

    def init(self, uid:int, title:str, text:str, descUrl:str, pictureUrl:str, items:list['ObjectItemInformationWithQuantity']):
        self.uid = uid
        self.title = title
        self.text = text
        self.descUrl = descUrl
        self.pictureUrl = pictureUrl
        self.items = items
        
        super().__init__()
    
    