from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


@dataclass
class PartyGuestInformations(NetworkMessage):
    guestId:int
    hostId:int
    name:str
    guestLook:EntityLook
    breed:int
    sex:bool
    status:PlayerStatus
    entities:list[PartyEntityBaseInformation]
    
    
    def __post_init__(self):
        super().__init__()
    