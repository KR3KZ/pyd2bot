from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch


class BreachBranchesMessage(INetworkMessage):
    protocolId = 2907
    branches:ExtendedBreachBranch
    
    
