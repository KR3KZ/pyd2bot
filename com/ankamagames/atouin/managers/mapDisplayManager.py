import logging

from com.ankamagames.jerakine.metaclasses.singleton import Singleton

logger = logging.getLogger("bot")

class MapDisplayManager(metaclass=Singleton):
   
   MEMORY_LOG:dict = dict(True)      
   
   _currentMap:WorldPoint
   
   _currentRenderId:int
   
   _isDefaultMap:bool
   
   _mapInstanceId:float = 0
   
   _lastMap:WorldPoint
   
   _currentMapRendered:bool = True
   
   _nMapLoadStart:int
   
   _nMapLoadEnd:int
   
   _nRenderMapStart:int
   
   _nRenderMapEnd:int
   
   matrix:Matrix
   
   def __init__(self):
      self.matrix = Matrix()
      super().__init__()
      self.init()
   
   @property
   def isDefaultMap(self) -> bool:
      return self._isDefaultMap
   
   @property
   def renderer(self) -> MapRenderer:
      return self._renderer
   
   @property
   def currentRenderId(self) -> int:
      return self._currentRenderId
   
   def fromMap(self, map:Map, decryptionKey:Bytelist = None, renderFixture:bool = True) -> int:
      self._currentMap = WorldPoint.fromMapId(map.id)
      rle:ResourceLoadedEvent = ResourceLoadedEvent(ResourceLoadedEvent.LOADED)
      rle.resource = map
      self.onMapLoaded(rle)
      return self._currentRenderId
   
   def display(self, pMap:WorldPoint, forceReloadWithoutCache:bool = False, decryptionKey:Bytelist = None, renderFixture:bool = True, displayWorld:bool = True) -> int:
      request:RenderRequest = RenderRequest(pMap,forceReloadWithoutCache,decryptionKey,renderFixture,displayWorld)
      logger.debug("Ask render map " + pMap.mapId + ", renderRequestID: " + request.renderId)
      self._renderRequestStack.append(request)
      self.checkForRender(displayWorld)
      return request.renderId
   
   def isBoundingBox(self, pictoId:int) -> bool:
      if MapRenderer.boundingBoxElements[pictoId]:
         return True
      return False
   
   def cacheAsBitmapEnabled(self, yes:bool) -> None:
      ls:list = MapRenderer.cachedAsBitmapElement
      num:int = len(ls)
      for i in range(0, num, 1):
         ls[i].cacheAsBitmap = yes
   
   @property
   def currentMapPoint(self) -> WorldPoint:
      return self._currentMap
   
   @property
   def currentMapRendered(self) -> bool:
      return self._currentMapRendered
   
   def getDataMapContainer(self) -> DataMapContainer:
      return self._currentDataMap
   
   @property
   def mapInstanceId(self) -> float:
      return self._mapInstanceId
   
   @mapInstanceId.setter
   def mapInstanceId(self, mapId:float) -> None:
      logger.debug("mapInstanceId " + mapId)
      self._mapInstanceId = mapId
   
   def activeIdentifiedElements(self, active:bool) -> None:
      ie:object = None
      identifiedElements:dict = self._renderer.identifiedElements
      for ie in identifiedElements:
         ie.sprite.mouseEnabled = active
   
   def unloadMap(self) -> None:
      self._renderer.unload()
   
   def getIdentifiedEntityElement(self, id:int) -> TiphonSprite:
      if self._renderer and self._renderer.identifiedElements and self._renderer.identifiedElements[id]:
         if isinstance(self._renderer.identifiedElements[id].sprite, TiphonSprite):
            return self._renderer.identifiedElements[id].sprite
      return None
   
   def getIdentifiedElement(self, id:int) -> Interactiveobject:
      if self._renderer and self._renderer.identifiedElements and self._renderer.identifiedElements[id]:
         return self._renderer.identifiedElements[id].sprite
      return None
   
   def getIdentifiedElementPosition(self, id:int) -> MapPoint:
      if self._renderer and self._renderer.identifiedElements and self._renderer.identifiedElements[id]:
         return self._renderer.identifiedElements[id].position
      return None
   
   def reset(self) -> None:
      self.unloadMap()
      self._currentMap = None
      logger.debug("mapInstanceId reset 0")
      self._mapInstanceId = 0
      self._currentMapRendered = True
      self._lastMap = None
      self._renderRequestStack = []
   
   def hideBackgroundForTacticMode(self, yes:bool, backgroundColor:int = 0) -> None:
      self._renderer.modeTactic(yes,backgroundColor)
   
   def init(self) -> None:
      self._renderRequestStack = []
      self._renderer = MapRenderer(Atouin().worldContainer,Elements())
      AdapterFactory.addAdapter("dlm",MapsAdapter)
      self._loader = ResourceLoaderFactory.getLoader(ResourceLoaderType.SERIAL_LOADER)
   
   def mapDisplayed(self) -> None:
      self._currentMapRendered = True
      InteractiveCellManager().updateInteractiveCell(self._currentDataMap)
      self._renderRequestStack.shift()
      msg:MapsLoadingCompleteMessage = MapsLoadingCompleteMessage(self._currentMap,MapDisplayManager().getDataMapContainer().dataMap)
      msg.renderRequestId = self._currentRenderId
      Atouin().handler.process(msg)
      self.checkForRender()
   
   def checkForRender(self, displayWorld:bool = True) -> None:
      dataMap:Map = None
      msg:MapsLoadingCompleteMessage = None
      atouin:Atouin = None
      if not self._currentMapRendered and self._currentMap:
         return
      if len(self._renderRequestStack) == 0:
         return
      request:RenderRequest = RenderRequest(self._renderRequestStack[0])
      pMap:WorldPoint = request.map
      forceReloadWithoutCache:bool = request.forceReloadWithoutCache
      Atouin().showWorld(displayWorld)
      self._renderer.initRenderContainer(Atouin().worldContainer)
      if not forceReloadWithoutCache and self._currentMap and self._currentMap.mapId == pMap.mapId and not Atouin().options.getOption("reloadLoadedMap"):
         self._renderRequestStack.shift()
         logger.debug("Map " + pMap.mapId + " is the same, renderRequestID: " + request.renderId)
         dataMap = MapDisplayManager().getDataMapContainer().dataMap
         msg = MapsLoadingCompleteMessage(self._currentMap,dataMap)
         atouin = Atouin()
         atouin.handler.process(msg)
         msg.renderRequestId = request.renderId
         atouin.applyMapZoomScale(dataMap)
         self.checkForRender()
         return
      self._currentMapRendered = False
      self._lastMap = self._currentMap
      self._currentMap = pMap
      self._currentRenderId = request.renderId
      self._forceReloadWithoutCache = forceReloadWithoutCache
      msg2:MapsLoadingStartedMessage = MapsLoadingStartedMessage()
      msg2.id = self._currentMap.mapId
      Atouin().handler.process(msg2)
      self._nMapLoadStart = getTimer()
      self._loader.cancel()
      self._loader.addEventListener(ResourceLoadedEvent.LOADED,self.onMapLoaded,False,0,True)
      self._loader.addEventListener(ResourceErrorEvent.ERROR,self.onMapFailed,False,0,True)
      self._loader.load(Uri(getMapUriFromId(pMap.mapId)),None)
   
   def onMapLoaded(self, e:ResourceLoadedEvent) -> None:
      self._loader.removeEventListener(ResourceLoadedEvent.LOADED,self.onMapLoaded)
      self._loader.removeEventListener(ResourceErrorEvent.ERROR,self.onMapFailed)
      request:RenderRequest = RenderRequest(self._renderRequestStack[0])
      self._nMapLoadEnd = getTimer()
      map:Map = Map()
      if isinstance(e.resource, Map):
         map = e.resource
      else:
         try:
            map.fromRaw(e.resource,request.decryptionKey)
         catch(err:Error)
            logger.fatal("Exception sur le parsing du fichier de map :\n" + err.getStackTrace())
            map = DefaultMap()
      self._isDefaultMap = map is DefaultMap
      self.unloadMap()
      DataMapProvider().resetUpdatedCell()
      DataMapProvider().resetSpecialEffects()
      if not request:
         return
      self._currentDataMap = DataMapContainer(map)
      MEMORY_LOG[DataMapContainer] = 1
      self._renderer.addEventListener(RenderMapEvent.GFX_LOADING_START,self.logGfxLoadTime,False,0,True)
      self._renderer.addEventListener(RenderMapEvent.GFX_LOADING_END,self.logGfxLoadTime,False,0,True)
      self._renderer.addEventListener(RenderMapEvent.MAP_RENDER_START,self.mapRendered,False,0,True)
      self._renderer.addEventListener(RenderMapEvent.MAP_RENDER_END,self.mapRendered,False,0,True)
      self._renderer.addEventListener(ProgressEvent.PROGRESS,self.mapRenderProgress,False,0,True)
      self._renderer.render(self._currentDataMap,self._forceReloadWithoutCache,request.renderId,request.renderFixture,request.displayWorld)
      FrustumManager().updateMap()
   
   def onMapFailed(self, e:ResourceErrorEvent) -> None:
      self._loader.removeEventListener(ResourceLoadedEvent.LOADED,self.onMapLoaded)
      self._loader.removeEventListener(ResourceErrorEvent.ERROR,self.onMapFailed)
      logger.error("Impossible de charger la map " + e.uri + " : " + e.errorMsg)
      self._currentMapRendered = True
      self._renderRequestStack.shift()
      self.checkForRender()
      self.signalMapLoadingFailure(MapLoadingFailedMessage.NO_FILE)
   
   def logGfxLoadTime(self, e:Event) -> None:
      if e.type == RenderMapEvent.GFX_LOADING_START:
         self._nGfxLoadStart = getTimer()
      if e.type == RenderMapEvent.GFX_LOADING_END:
         self._nGfxLoadEnd = getTimer()
   
   def tweenInterMap(self, e:Event) -> None:
      self._screenshot.alpha -= self._screenshot.alpha / 3
      if self._screenshot.alpha < 0.01:
         Atouin().worldContainer.cacheAsBitmap = False
         self.removeScreenShot()
         EnterFrameDispatcher.removeEventListener(self.tweenInterMap)
   
   def mapRenderProgress(self, e:ProgressEvent) -> None:
      if not self._currentMap:
         self._currentMapRendered = True
         self.unloadMap()
         self.signalMapLoadingFailure(MapLoadingFailedMessage.CLIENT_SHUTDOWN)
         return
      msg:MapRenderProgressMessage = MapRenderProgressMessage(e.bytesLoaded / e.bytesTotal * 100)
      msg.id = self._currentMap.mapId
      msg.renderRequestId = self._currentRenderId
      Atouin().handler.process(msg)
   
   def signalMapLoadingFailure(self, errorReasonId:int) -> None:
      msg:MapLoadingFailedMessage = MapLoadingFailedMessage()
      if not self._currentMap:
         msg.id = 0
      else:
         msg.id = self._currentMap.mapId
      msg.errorReason = errorReasonId
      Atouin().handler.process(msg)
   
   def mapRendered(self, e:RenderMapEvent) -> None:
      tt:int = 0
      tml:int = 0
      tgl:int = 0
      msg:MapLoadedMessage = None
      if e.type == RenderMapEvent.MAP_RENDER_START:
         self._nRenderMapStart = getTimer()
      if e.type == RenderMapEvent.MAP_RENDER_END:
         self.removeRendererListeners()
         self.mapDisplayed()
         self._nRenderMapEnd = getTimer()
         tt = self._nRenderMapEnd - self._nMapLoadStart
         tml = self._nMapLoadEnd - self._nMapLoadStart
         tgl = self._nGfxLoadEnd - self._nGfxLoadStart
         msg = MapLoadedMessage()
         msg.dataLoadingTime = tml
         msg.gfxLoadingTime = tgl
         msg.renderingTime = self._nRenderMapEnd - self._nRenderMapStart
         msg.globalRenderingTime = tt
         logger.info("map rendered [total : " + tt + "ms, " + (tt < 100 ? " " + (tt < 10 ? " " : "") : "") + "map load : " + tml + "ms, " + (tml < 100 ? " " + (tml < 10 ? " " : "") : "") + "gfx load : " + tgl + "ms, " + (tgl < 100 ? " " + (tgl < 10 ? " " : "") : "") + "render : " + (self._nRenderMapEnd - self._nRenderMapStart) + "ms] file : " + (!not self._currentMap ? str(self._currentMap.mapId) : "???") + ".dlm" + (!not self._isDefaultMap ? " (/!\\ DEFAULT MAP) " : "") + " / renderRequestID #" + self._currentRenderId)
         if self._screenshot and self._screenshot.parent:
            if Atouin().options.getOption(EnterFrameConst.TWEENT_INTER_MAP):
               Atouin().worldContainer.cacheAsBitmap = True
               EnterFrameDispatcher.addEventListener(self.tweenInterMap,EnterFrameConst.TWEENT_INTER_MAP)
            else:
               self.removeScreenShot()
         msg.id = self._currentMap.mapId
         Atouin().handler.process(msg)
   
   def removeRendererListeners(self) -> None:
      self._renderer.removeEventListener(RenderMapEvent.GFX_LOADING_START,self.logGfxLoadTime)
      self._renderer.removeEventListener(RenderMapEvent.GFX_LOADING_END,self.logGfxLoadTime)
      self._renderer.removeEventListener(RenderMapEvent.MAP_RENDER_START,self.mapRendered)
      self._renderer.removeEventListener(RenderMapEvent.MAP_RENDER_END,self.mapRendered)
      self._renderer.removeEventListener(ProgressEvent.PROGRESS,self.mapRenderProgress)
   
   def removeScreenShot(self) -> None:
      self._screenshot.parent.removeChild(self._screenshot)
      self._screenshotData.fillRect(Rectangle(0,0,self._screenshotData.width,self._screenshotData.height),4278190080)
