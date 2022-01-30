from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    protocolId = 9272
    memberId:int
    active:bool
    
