from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class SetUpdateMessage(NetworkMessage):
    setId:int
    setObjects:list[int]
    setEffects:list['ObjectEffect']
    

    def init(self, setId:int, setObjects:list[int], setEffects:list['ObjectEffect']):
        self.setId = setId
        self.setObjects = setObjects
        self.setEffects = setEffects
        
        super().__init__()
    
    