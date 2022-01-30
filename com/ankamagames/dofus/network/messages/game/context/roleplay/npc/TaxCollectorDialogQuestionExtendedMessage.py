from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage


class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
    protocolId = 625
    maxPods:int
    prospecting:int
    wisdom:int
    taxCollectorsCount:int
    taxCollectorAttack:int
    kamas:float
    experience:float
    pods:int
    itemsValue:float
    
