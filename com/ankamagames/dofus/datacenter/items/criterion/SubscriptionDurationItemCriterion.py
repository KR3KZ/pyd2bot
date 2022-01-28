               
   class SubscriptionDurationItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = PatternDecoder.combine(I18n.getUiText("ui.social.daysSinceLastConnection",[_criterionValue]),"n",_criterionValue <= 1,_criterionValue == 0)
         readableCriterionRef:str = I18n.getUiText("ui.veteran.totalSubscriptionDuration")
         return readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return SubscriptionDurationItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         return math.floor(PlayerManager().subscriptionDurationElapsed / (24 * 60 * 60))
