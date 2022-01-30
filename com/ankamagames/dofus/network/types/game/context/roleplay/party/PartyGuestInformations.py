from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


class PartyGuestInformations(INetworkMessage):
    protocolId = 1057
    guestId:int
    hostId:int
    name:str
    guestLook:EntityLook
    breed:int
    sex:bool
    status:PlayerStatus
    entities:PartyEntityBaseInformation
    
    
