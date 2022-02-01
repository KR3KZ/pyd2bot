from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.alignment.war.effort.AlignmentWarEffortInformation import AlignmentWarEffortInformation


class AlignmentWarEffortProgressionMessage(NetworkMessage):
    effortProgressions:list[AlignmentWarEffortInformation]
    
    
