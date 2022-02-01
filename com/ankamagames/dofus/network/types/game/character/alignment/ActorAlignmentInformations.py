from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActorAlignmentInformations(INetworkMessage):
    protocolId = 3635
    alignmentSide:int
    alignmentValue:int
    alignmentGrade:int
    characterPower:int
    
    
