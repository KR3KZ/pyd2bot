from com.ankamagames.atouin.Atouin import Atouin
from com.ankamagames.atouin.AtouinConstants import AtouinConstants
from com.ankamagames.atouin.data.map.CellData import CellData
from com.ankamagames.atouin.data.map.Layer import Layer
from com.ankamagames.atouin.messages.CellClickMessage import CellClickMessage
from com.ankamagames.atouin.messages.CellOutMessage import CellOutMessage
from com.ankamagames.atouin.messages.CellOverMessage import CellOverMessage
from com.ankamagames.atouin.renderers.TrapZoneRenderer import TrapZoneRenderer
from com.ankamagames.atouin.renderers.ZoneDARenderer import ZoneDARenderer
from com.ankamagames.atouin.types.CellContainer import CellContainer
from com.ankamagames.atouin.types.CellReference import CellReference
from com.ankamagames.atouin.types.DataMapContainer import DataMapContainer
from com.ankamagames.atouin.types.DebugToolTip import DebugToolTip
from com.ankamagames.atouin.types.GraphicCell import GraphicCell
from com.ankamagames.atouin.types.LayerContainer import LayerContainer
from com.ankamagames.atouin.types.Selection import Selection
from com.ankamagames.atouin.utils.CellIdConverter import CellIdConverter
from com.ankamagames.atouin.utils.CellUtil import CellUtil
from com.ankamagames.atouin.utils.DataMapProvider import DataMapProvider
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.entities.interfaces.IMovable import IMovable
from com.ankamagames.jerakine.logger.Log import Log
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.Color import Color
from com.ankamagames.jerakine.types.events.PropertyChangeEvent import PropertyChangeEvent
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint
from com.ankamagames.jerakine.types.zones.Lozenge import Lozenge
from com.ankamagames.jerakine.utils.display.StageShareManager import StageShareManager
from com.ankamagames.jerakine.utils.errors.SingletonError import SingletonError


class InteractiveCellManager:
   
   logger = Logger(__name__)
   
   _self:InteractiveCellManager
   
   
   _cellOverEnabled:bool = False
   
   _aCells:list
   
   _aCellPool:list
   
   _bShowGrid:bool
   
   _showEveryCellId:bool
   
   _isInFight:bool = False
   
   _interaction_click:bool
   
   _interaction_out:bool
   
   _trapZoneRenderer:TrapZoneRenderer
   
   def __init__(self):
      self._aCellPool = list()
      self._bShowGrid = Atouin().options.getOption("alwaysShowGrid")
      self._showEveryCellId = Atouin().options.getOption("showEveryCellId")
      super().__init__()
      if _self:
         raise SingletonError()
      self.init()
   
   def getInstance(self) -> InteractiveCellManager:
      if not _self:
         _self = InteractiveCellManager()
      return _self
   
   @property
   def cellOverEnabled(self) -> bool:
      return self._cellOverEnabled
   
   @cellOverEnabled.setter
   def cellOverEnabled(self, value:bool) -> None:
      self.overStateChanged(self._cellOverEnabled,value)
      self._cellOverEnabled = value
   
   @property
   def cellOutEnabled(self) -> bool:
      return self._interaction_out
   
   @property
   def cellClickEnabled(self) -> bool:
      return self._interaction_click
   
   def initManager(self) -> None:
      self._aCells = list()
      Atouin().options.addEventListener(PropertyChangeEvent.PROPERTY_CHANGED,self.onPropertyChanged)
   
   def setInteraction(self, click:bool = True, over:bool = False, out:bool = False, updateHavenbagCellVisibility:bool = False, visible:bool = True) -> None:
      cell:GraphicCell = None
      self._interaction_click = click
      self._cellOverEnabled = over
      self._interaction_out = out
      for cell in self._aCells:
         if click:
            cell.addEventListener(MouseEvent.CLICK,self.mouseClick)
         else:
            cell.removeEventListener(MouseEvent.CLICK,self.mouseClick)
         if over:
            cell.addEventListener(MouseEvent.MOUSE_OVER,self.mouseOver)
         else:
            cell.removeEventListener(MouseEvent.MOUSE_OVER,self.mouseOver)
         if out:
            cell.addEventListener(MouseEvent.MOUSE_OUT,self.mouseOut)
         else:
            cell.removeEventListener(MouseEvent.MOUSE_OUT,self.mouseOut)
         cell.mouseEnabled = click or over or out
         if updateHavenbagCellVisibility and CellData(MapDisplayManager().getDataMapContainer().dataMap.cells[cell.cellId]).havenbagCell:
            cell.visible = visible
   
   def getCell(self, cellId:int) -> GraphicCell:
      if cellId > CellUtil.MAX_CELL_ID or cellId < CellUtil.MIN_CELL_ID:
         return null
      self._aCells[cellId] = self._aCellPool[cellId]
      return self._aCells[cellId]
   
   def updateInteractiveCell(self, container:DataMapContainer) -> None:
      cellRef:CellReference = None
      gCell:GraphicCell = None
      cellCtr:CellContainer = None
      if not container:
         logger.error("Can\'t update interactive cell of a NULL container")
         return
      self.setInteraction(True,Atouin().options.getOption("showCellIdOnOver"),Atouin().options.getOption("showCellIdOnOver"))
      self.showEveryCellId(Atouin().options.getOption("showEveryCellId"))
      aCell:list = container.getCell()
      showTransitions:bool = Atouin().options.getOption("showTransitions")
      alpha:float = self._bShowGrid or Atouin().options.getOption("alwaysShowGrid") ? Number(1) : Number(0)
      if self._showEveryCellId and alpha == 0:
         alpha = 0.8
      layer:LayerContainer = container.getLayer(Layer.LAYER_DECOR)
      cellIndex:int = 0
      cellIndexMax:int = len(self._aCells)
      ind:int = 0
      currentCell:GraphicCell = self._aCells[0]
      if not currentCell:
         while(not currentCell and cellIndex < cellIndexMax)
            currentCell = self._aCells[cellIndex += 1]
         cellIndex--
      while(ind < layer.numChildren and cellIndex < cellIndexMax)
         cellCtr = layer.getChildAt(ind) as CellContainer
         if currentCell != null and (cellCtr and currentCell.cellId <= cellCtr.cellId):
            cellRef = aCell[cellIndex]
            gCell = self._aCells[cellIndex]
            gCell.y = cellRef.elevation
            gCell.visible = cellRef.mov and not cellRef.isDisabled
            gCell.alpha = alpha
            layer.addChildAt(gCell,ind)
            currentCell = self._aCells[ += 1cellIndex]
         ind += 1
   
   def updateCell(self, cellId:int, enabled:bool) -> bool:
      DataMapProvider().updateCellMovLov(cellId,enabled)
      if self._aCells[cellId] != null:
         self._aCells[cellId].visible = enabled
         return True
      return False
   
   def updateCellElevation(self, cellId:int, elevation:int) -> None:
      if not self._aCells[cellId].initialElevation:
         self._aCells[cellId].initialElevation = self._aCells[cellId].y
      self._aCells[cellId].y = self._aCells[cellId].initialElevation - elevation
   
   def resetHavenbagCellsVisibility(self) -> None:
      cell:GraphicCell = None
      for cell in self._aCells:
         if cell and MapDisplayManager().getDataMapContainer().dataMap.cells[cell.cellId].havenbagCell:
            cell.visible = True
   
   def show(self, b:bool, pIsInFight:bool = False) -> None:
      cell:GraphicCell = None
      self._bShowGrid = b
      self._isInFight = pIsInFight
      alpha:float = self._bShowGrid or Atouin().options.getOption("alwaysShowGrid") ? Number(1) : Number(0)
      cellsData:list[CellData] = MapDisplayManager().getDataMapContainer().dataMap.cells
      for(i:int = 0 i < len(self._aCells) i += 1)
         cell = GraphicCell(self._aCells[i])
         if cell:
            if pIsInFight:
               cell.buttonMode = not cellsData[i].nonWalkableDuringFight
            else:
               cell.buttonMode = not cellsData[i].nonWalkableDuringRP
            if pIsInFight and alpha == 1 and cellsData[i].nonWalkableDuringFight:
               cell.alpha = 0
            else:
               cell.alpha = alpha
            if cell.numChildren > 1 and cell.alpha == 0:
               cell.alpha = 0.8
   
   def showEveryCellId(self, b:bool) -> None:
      cell:GraphicCell = None
      tf_id:TextField = None
      glow:GlowFilter = None
      self._showEveryCellId = b
      for(i:int = 0 i < len(self._aCells) i += 1)
         cell = GraphicCell(self._aCells[i])
         if cell:
            if self._showEveryCellId:
               if cell.alpha == 0:
                  cell.alpha = 0.8
               while(cell.numChildren > 1)
                  cell.removeChildAt(1)
               tf_id = TextField()
               tf_id.text = "" + i
               tf_id.autoSize = TextFieldAutoSize.CENTER
               tf_id.width = 30
               tf_id.height = 20
               tf_id.x = cell.width / 2 - tf_id.width / 2
               tf_id.y = tf_id.height / 2
               glow = GlowFilter(16777215,0.8,8,8,6,2)
               tf_id.filters = [glow]
               cell.addChild(tf_id)
            else:
               while(cell.numChildren > 1)
                  cell.removeChildAt(1)
               if cell.alpha != 0 and cell.alpha != 1:
                  cell.alpha = 0
   
   def clean(self) -> None:
      i:int = 0
      if self._aCells:
         for(i = 0 i < len(self._aCells) i += 1)
            if self._aCells[i]:
               while(self._aCells[i].numChildren > 1)
                  self._aCells[i].removeChildAt(1)
               if self._aCells[i].parent:
                  self._aCells[i].parent.removeChild(self._aCells[i])
   
   def init(self) -> None:
      c:GraphicCell = None
      for(i:int = 0 i < AtouinConstants.MAP_CELLS_COUNT i += 1)
         c = GraphicCell(i)
         c.mouseEnabled = False
         c.mouseChildren = False
         self._aCellPool[i] = c
   
   def overStateChanged(self, oldValue:bool, newValue:bool) -> None:
      if oldValue == newValue:
         return
      if not oldValue and newValue:
         self.registerOver(True)
      elif oldValue and not newValue:
         self.registerOver(False)
   
   def registerOver(self, enabled:bool) -> None:
      for(i:int = 0 i < AtouinConstants.MAP_CELLS_COUNT i += 1)
         if self._aCells[i]:
            if enabled:
               self._aCells[i].addEventListener(MouseEvent.ROLL_OVER,self.mouseOver)
               self._aCells[i].addEventListener(MouseEvent.ROLL_OUT,self.mouseOut)
            else:
               self._aCells[i].removeEventListener(MouseEvent.ROLL_OVER,self.mouseOver)
               self._aCells[i].removeEventListener(MouseEvent.ROLL_OUT,self.mouseOut)
   
   def mouseClick(self, e:MouseEvent) -> None:
      a:list = None
      entity:IEntity = None
      msg:CellClickMessage = None
      target:Sprite = Sprite(e.target)
      if not target.parent:
         return
      index:int = target.parent.getChildIndex(target)
      cellId:int = parseInt(target.name)
      cellCoordinates:Point = CellIdConverter.cellIdToCoord(cellId)
      if not DataMapProvider().pointCanStop(cellCoordinates.x,cellCoordinates.y):
         logger.info("Cannot move to self cell in RP")
         return
      if Atouin().options.getOption("virtualPlayerJump"):
         a = EntitiesManager().entities
         for entity in a:
            if isinstance(entity, IMovable):
               IMovable(entity).jump(MapPoint.fromCellId(cellId))
      else:
         msg = CellClickMessage()
         msg.cellContainer = target
         msg.cellDepth = index
         msg.cell = MapPoint.fromCoords(cellCoordinates.x,cellCoordinates.y)
         msg.cellId = cellId
         Atouin().handler.process(msg)
   
   def mouseOver(self, e:MouseEvent) -> None:
      _cellColor:int = 0
      textInfo = None
      mp:MapPoint = None
      cellData:CellData = None
      sel:Selection = None
      target:Sprite = Sprite(e.target)
      if not target.parent:
         return
      index:int = target.parent.getChildIndex(target)
      cellId:int = parseInt(target.name)
      cellCoordinates:Point = CellIdConverter.cellIdToCoord(cellId)
      if Atouin().options.getOption("showCellIdOnOver"):
         _cellColor = 0
         textInfo = target.name + " (" + cellCoordinates.x + "/" + cellCoordinates.y + ")"
         mp = MapPoint.fromCoords(cellCoordinates.x,cellCoordinates.y)
         textInfo += "\nLigne de vue : " + not DataMapProvider().pointLos(mp.x,mp.y)
         textInfo += "\nBlocage �diteur : " + not DataMapProvider().pointMov(mp.x,mp.y)
         textInfo += "\nBlocage entit�e : " + not DataMapProvider().pointMov(mp.x,mp.y,False)
         textInfo += "\nfarmCell : " + DataMapProvider().farmCell(mp.x,mp.y)
         textInfo += "\nhavenbagCell : " + DataMapProvider().cellByCoordsIsHavenbagCell(mp.x,mp.y)
         cellData = CellData(MapDisplayManager().getDataMapContainer().dataMap.cells[cellId])
         textInfo += "\nForcage fleche bas : " + cellData.useBottomArrow
         textInfo += "\nForcage fleche haut : " + cellData.useTopArrow
         textInfo += "\nForcage fleche droite : " + cellData.useRightArrow
         textInfo += "\nForcage fleche gauche : " + cellData.useLeftArrow
         textInfo += "\nID de zone : " + cellData.moveZone
         textInfo += "\nHauteur : " + cellData.floor + " px"
         textInfo += "\nSpeed : " + cellData.speed
         DebugToolTip().text = textInfo
         sel = SelectionManager().getSelection("infoOverCell")
         if not sel:
            sel = Selection()
            sel.color = Color(_cellColor)
            sel.renderer = ZoneDARenderer()
            sel.zone = Lozenge(0,0,DataMapProvider())
            SelectionManager().addSelection(sel,"infoOverCell",cellId)
         else:
            SelectionManager().update("infoOverCell",cellId)
         StageShareManager.stage.addChild(DebugToolTip())
      msg:CellOverMessage = CellOverMessage()
      msg.cellContainer = target
      msg.cellDepth = index
      msg.cell = MapPoint.fromCoords(cellCoordinates.x,cellCoordinates.y)
      msg.cellId = cellId
      Atouin().handler.process(msg)
   
   def mouseOut(self, e:MouseEvent) -> None:
      target:Sprite = Sprite(e.target)
      if not target.parent:
         return
      index:int = target.parent.getChildIndex(target)
      cellId:int = parseInt(target.name)
      cellCoordinates:Point = CellIdConverter.cellIdToCoord(cellId)
      if Atouin().worldContainer.contains(DebugToolTip()):
         Atouin().worldContainer.removeChild(DebugToolTip())
      msg:CellOutMessage = CellOutMessage()
      msg.cellContainer = target
      msg.cellDepth = index
      msg.cell = MapPoint.fromCoords(cellCoordinates.x,cellCoordinates.y)
      msg.cellId = cellId
      Atouin().handler.process(msg)
   
   def onPropertyChanged(self, e:PropertyChangeEvent) -> None:
      if e.propertyName == "alwaysShowGrid":
         self.show(e.propertyValue,self._isInFight)
