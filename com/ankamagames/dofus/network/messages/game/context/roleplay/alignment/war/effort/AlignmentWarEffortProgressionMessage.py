from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation


class AlignmentWarEffortProgressionMessage(NetworkMessage):
    protocolId = 2084
    effortProgressions:AlignmentWarEffortInformation
    
