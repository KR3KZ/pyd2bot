               
class AllianceRightsItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def isRespected(self) -> bool:
      hasThisRight:bool = False
      if not AllianceFrame().hasAlliance:
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            return True
         return False
      alliance:AllianceWrapper = AllianceFrame().alliance
      switch(criterionValue)
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_BOSS:
            hasThisRight = alliance.isBoss
            break
         default:
            hasThisRight = True
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            return hasThisRight
         case ItemCriterionOperator.DIFFERENT:
            return not hasThisRight
         default:
            return False
   
   @property
   def text(self) -> str:
      readableCriterion:str = None
      readableCriterionValue:str = None
      switch(criterionValue)
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_BOSS:
            readableCriterionValue = I18n.getUiText("ui.guild.right.leader")
            break
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_KICK_GUILDS:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsBann")
            break
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_MANAGE_PRISMS:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsSetAlliancePrism")
            break
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_MANAGE_RIGHTS:
            readableCriterionValue = I18n.getUiText("ui.social.guildManageRights")
            break
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_RECRUIT_GUILDS:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsInvit")
            break
         case AllianceRightsBitEnum.ALLIANCE_RIGHT_TALK_IN_CHAN:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsTalkInAllianceChannel")
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText("ui.criterion.allianceRights",[readableCriterionValue])
            break
         case ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.criterion.notAllianceRights",[readableCriterionValue])
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return AllianceRightsItemCriterion(self.basicText)
