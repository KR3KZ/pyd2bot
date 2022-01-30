from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanInformations(INetworkMessage):
    protocolId = 7547
    restrictions:ActorRestrictionsInformations
    sex:bool
    options:HumanOption
    
    
