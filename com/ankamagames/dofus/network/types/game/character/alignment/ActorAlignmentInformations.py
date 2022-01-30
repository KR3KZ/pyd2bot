from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ActorAlignmentInformations(INetworkMessage):
    protocolId = 3635
    alignmentSide:int
    alignmentValue:int
    alignmentGrade:int
    characterPower:int
    
    
