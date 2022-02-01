from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    memberId:int
    active:bool
    
    
