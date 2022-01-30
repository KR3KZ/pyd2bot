from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation


class AlignmentWarEffortProgressionMessage(INetworkMessage):
    protocolId = 2084
    effortProgressions:AlignmentWarEffortInformation
    
    
