from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch


class BreachBranchesMessage(NetworkMessage):
    branches:list[ExtendedBreachBranch]
    
    
