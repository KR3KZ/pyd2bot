      
   class ItemCriterionOperator(IDataCenter):
      
      SUPERIOR:str = ">"
      
      INFERIOR:str = "<"
      
      EQUAL:str = "="
      
      DIFFERENT:str = "!"
      
      OPERATORS_LIST:list = [SUPERIOR,INFERIOR,EQUAL,DIFFERENT,"#","~","s","S","e","E","v","i","X","/"]
       
      
      _operator:str
      
      def __init__(self, pstrOperator:str):
         super().__init__()
         self._operator = pstrOperator
      
      @property
      def text(self) -> str:
         return self._operator
      
      @property
      def htmlText(self) -> str:
         if self._operator == SUPERIOR:
            return "&gt"
         if self._operator == INFERIOR:
            return "&lt"
         return self._operator
      
      def compare(self, pLeftMember:float, pRightMember:float) -> bool:
         switch(self._operator)
            case SUPERIOR:
               if pLeftMember > pRightMember:
                  return True
               break
            case INFERIOR:
               if pLeftMember < pRightMember:
                  return True
               break
            case EQUAL:
               if pLeftMember == pRightMember:
                  return True
               break
            case DIFFERENT:
               if pLeftMember != pRightMember:
                  return True
               break
         return False
