from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceInvitationStateRecruterMessage(NetworkMessage):
    recrutedName:str
    invitationState:int
    

    def init(self, recrutedName:str, invitationState:int):
        self.recrutedName = recrutedName
        self.invitationState = invitationState
        
        super().__init__()
    
    