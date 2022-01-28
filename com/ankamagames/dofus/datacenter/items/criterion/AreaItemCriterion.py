               
   class AreaItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def isRespected(self) -> bool:
         switch(_operator.text)
            case ItemCriterionOperator.EQUAL:
            case ItemCriterionOperator.DIFFERENT:
               return super().isRespected
            default:
               return False
      
      @property
      def text(self) -> str:
         readableCriterion:str = None
         area:Area = Area.getAreaById(_criterionValue)
         if not area:
            return "error on AreaItemCriterion"
         areaName:str = area.name
         switch(_operator.text)
            case ItemCriterionOperator.EQUAL:
               readableCriterion = I18n.getUiText("ui.tooltip.beInArea",[areaName])
               break
            case ItemCriterionOperator.DIFFERENT:
               readableCriterion = I18n.getUiText("ui.tooltip.dontBeInArea",[areaName])
         return readableCriterion
      
      def clone(self) -> IItemCriterion:
         return AreaItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         return PlayedCharacterManager().currentSubArea.area.id
