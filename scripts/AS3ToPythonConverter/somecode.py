    def pushed(self) -> bool:
        ccFrame:ContextChangeFrame = None
        connexion:str = None
        mirmsg:MapInformationsRequestMessage = None
        self.initNewMap()
        self._playersId = list()
        self._merchantsList = list()
        self._monstersIds = list[float]()
        self._emoteTimesBySprite = dict()
        _entitiesVisiblefloat = 0
        self._auraCycleIndex = 0
        self._auraCycleTimer = BenchmarkTimer(1800,0,"RoleplayEntitiesFrame._auraCycleTimer")
        if OptionManager.getOptionManager("tiphon").getOption("auraMode") == OptionEnum.AURA_CYCLE:
            self._auraCycleTimer.addEventListener(TimerEvent.TIMER,self.onAuraCycleTimer)
            self._auraCycleTimer.start()
        if MapDisplayManager().currentMapRendered:
            ccFrame = Kernel.getWorker().getFrame(ContextChangeFrame) as ContextChangeFrame
            connexion = ""
            if ccFrame:
                connexion = ccFrame.mapChangeConnexion
            mirmsg = MapInformationsRequestMessage()
            mirmsg.initMapInformationsRequestMessage(MapDisplayManager().currentMapPoint.mapId)
            ConnectionsHandler.getConnection().send(mirmsg,connexion)
        else
            self._waitForMap = True
        self._loader = ResourceLoaderFactory.getLoader(ResourceLoaderType.PARALLEL_LOADER)
        self._loader.addEventListener(ResourceLoadedEvent.LOADED,self.onGroundObjectLoaded)
        self._loader.addEventListener(ResourceErrorEvent.ERROR,self.onGroundObjectLoadFailed)
        _interactiveElements = list[InteractiveElement]()
        Dofus().options.addEventListener(PropertyChangeEvent.PROPERTY_CHANGED,self.onPropertyChanged)
        Tiphon().options.addEventListener(PropertyChangeEvent.PROPERTY_CHANGED,self.onTiphonPropertyChanged)
        self._allianceFrame = Kernel.getWorker().getFrame(AllianceFrame) as AllianceFrame
        return super().appended()
