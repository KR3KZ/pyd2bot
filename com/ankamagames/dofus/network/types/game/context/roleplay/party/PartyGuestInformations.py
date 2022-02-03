from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    


class PartyGuestInformations(NetworkMessage):
    guestId:int
    hostId:int
    name:str
    guestLook:'EntityLook'
    breed:int
    sex:bool
    status:'PlayerStatus'
    entities:list['PartyEntityBaseInformation']
    

    def init(self, guestId:int, hostId:int, name:str, guestLook:'EntityLook', breed:int, sex:bool, status:'PlayerStatus', entities:list['PartyEntityBaseInformation']):
        self.guestId = guestId
        self.hostId = hostId
        self.name = name
        self.guestLook = guestLook
        self.breed = breed
        self.sex = sex
        self.status = status
        self.entities = entities
        
        super().__init__()
    
    