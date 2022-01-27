                                 
   class ItemCriterion(IItemCriterion, IDataCenter):
      
      logger = logging.getLogger("bot")
       
      
      _serverCriterionForm:str
      
      _operator:ItemCriterionOperator
      
      _criterionRef:str
      
      _criterionValue:int
      
      _criterionValueText:str
      
      def __init__(self, pCriterion:str):
         super().__init__()
         self._serverCriterionForm = pCriterion
         self.getInfos()
      
      @property
      def inlineCriteria(self) -> list[IItemCriterion]:
         criteria:list[IItemCriterion] = list[IItemCriterion]()
         criteria.append(self)
         return criteria
      
      @property
      def criterionValue(self) -> Object:
         return self._criterionValue
      
      @property
      def operatorText(self) -> str:
         return !not self._operator ? self._operator.text : None
      
      @property
      def operator(self) -> ItemCriterionOperator:
         return self._operator
      
      @property
      def isRespected(self) -> bool:
         player:PlayedCharacterManager = PlayedCharacterManager()
         if not player or not player.characteristics:
            return True
         return self._operator.compare(self.getCriterion(),self._criterionValue)
      
      @property
      def text(self) -> str:
         return self.buildText(False)
      
      @property
      def textForTooltip(self) -> str:
         return self.buildText(True)
      
      @property
      def basicText(self) -> str:
         return self._serverCriterionForm
      
      def clone(self) -> IItemCriterion:
         return ItemCriterion(self.basicText)
      
      def buildText(self, forTooltip:bool = False) -> str:
         readableCriterionRef:str = None
         knownCriteriaList:list = None
         index:int = 0
         switch(self._criterionRef)
            case "CM":
               readableCriterionRef = I18n.getUiText("ui.stats.movementPoints")
               break
            case "CP":
               readableCriterionRef = I18n.getUiText("ui.stats.actionPoints")
               break
            case "CH":
               readableCriterionRef = I18n.getUiText("ui.pvp.honourPoints")
               break
            case "CD":
               readableCriterionRef = I18n.getUiText("ui.pvp.disgracePoints")
               break
            case "CT":
               readableCriterionRef = I18n.getUiText("ui.stats.takleBlock")
               break
            case "Ct":
               readableCriterionRef = I18n.getUiText("ui.stats.takleEvade")
               break
            default:
               knownCriteriaList = ["CS","Cs","CV","Cv","CA","Ca","CI","Ci","CW","Cw","CC","Cc","PG","PJ","Pj","PM","PA","PN","PE","<NO>","PS","PR","PL","PK","Pg","Pr","Ps","Pa","PP","PZ","CM","Qa","CP","ca","cc","ci","cs","cv","cw","Pl"]
               index = knownCriteriaList.index(self._criterionRef)
               if index > -1:
                  readableCriterionRef = I18n.getUiText("ui.item.characteristics").split(",")[index]
               else:
                  _log.warn("Unknown criteria \'" + self._criterionRef + "\'")
         if forTooltip:
            return index > -1 ? readableCriterionRef + " " + "<span class=\'#valueCssClass\'>" + self._operator.text + " " + self._criterionValue + "</span>" : None:
         return readableCriterionRef + " " + self._operator.text + " " + self._criterionValue
      
      def getInfos(self) -> None:
         operator:str = None
         for operator in ItemCriterionOperator.OPERATORS_LIST:
            if self._serverCriterionForm.index(operator) == 2:
               self._operator = ItemCriterionOperator(operator)
               self._criterionRef = self._serverCriterionForm.split(operator)[0]
               self._criterionValue = self._serverCriterionForm.split(operator)[1]
               self._criterionValueText = self._serverCriterionForm.split(operator)[1]
               break
      
      def getCriterion(self) -> int:
         criterion:int = 0
         player:PlayedCharacterManager = PlayedCharacterManager()
         statsManager:StatsManager = StatsManager()
         if statsManager == None:
            return 0
         stats:EntityStats = statsManager.getStats(player.id)
         if stats == None:
            return 0
         switch(self._criterionRef)
            case "Ca":
               criterion = stats.getStatBaseValue(StatIds.AGILITY)
               break
            case "CA":
               criterion = stats.getStatTotalValue(StatIds.AGILITY)
               break
            case "Cc":
               criterion = stats.getStatBaseValue(StatIds.CHANCE)
               break
            case "CC":
               criterion = stats.getStatTotalValue(StatIds.CHANCE)
               break
            case "Ce":
               criterion = stats.getStatBaseValue(StatIds.ENERGY_POINTS)
               break
            case "CE":
               criterion = stats.getStatTotalValue(StatIds.MAX_ENERGY_POINTS)
               break
            case "CH":
               criterion = stats.getStatTotalValue(StatIds.HONOUR_POINTS)
               break
            case "Ci":
               criterion = stats.getStatBaseValue(StatIds.INTELLIGENCE)
               break
            case "CI":
               criterion = stats.getStatTotalValue(StatIds.INTELLIGENCE)
               break
            case "CL":
               criterion = stats.getHealthPoints()
               break
            case "CM":
               criterion = stats.getStatTotalValue(StatIds.MOVEMENT_POINTS)
               break
            case "CP":
               criterion = stats.getStatTotalValue(StatIds.ACTION_POINTS)
               break
            case "Cs":
               criterion = stats.getStatBaseValue(StatIds.STRENGTH)
               break
            case "CS":
               criterion = stats.getStatTotalValue(StatIds.STRENGTH)
               break
            case "Cv":
               criterion = stats.getStatBaseValue(StatIds.VITALITY)
               break
            case "CV":
               criterion = stats.getStatTotalValue(StatIds.VITALITY)
               break
            case "Cw":
               criterion = stats.getStatBaseValue(StatIds.WISDOM)
               break
            case "CW":
               criterion = stats.getStatTotalValue(StatIds.WISDOM)
               break
            case "Ct":
               criterion = stats.getStatTotalValue(StatIds.TACKLE_EVADE)
               break
            case "CT":
               criterion = stats.getStatTotalValue(StatIds.TACKLE_BLOCK)
               break
            case "ca":
               criterion = stats.getStatAdditionalValue(StatIds.AGILITY)
               break
            case "cc":
               criterion = stats.getStatAdditionalValue(StatIds.CHANCE)
               break
            case "ci":
               criterion = stats.getStatAdditionalValue(StatIds.INTELLIGENCE)
               break
            case "cs":
               criterion = stats.getStatAdditionalValue(StatIds.STRENGTH)
               break
            case "cv":
               criterion = stats.getStatAdditionalValue(StatIds.VITALITY)
               break
            case "cw":
               criterion = stats.getStatAdditionalValue(StatIds.WISDOM)
         return criterion
