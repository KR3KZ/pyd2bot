from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActorAlignmentInformations(NetworkMessage):
    protocolId = 3635
    alignmentSide:int
    alignmentValue:int
    alignmentGrade:int
    characterPower:float
    
