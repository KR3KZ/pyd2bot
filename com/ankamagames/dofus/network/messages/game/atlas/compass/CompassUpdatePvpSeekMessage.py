from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
    protocolId = 5714
    memberId:float
    memberName:str
    
