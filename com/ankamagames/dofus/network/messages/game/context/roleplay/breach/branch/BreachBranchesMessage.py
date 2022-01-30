from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch


class BreachBranchesMessage(NetworkMessage):
    protocolId = 2907
    branches:ExtendedBreachBranch
    
    
