DOFUSINVOKER = C:\\Users\\majdoub\\AppData\\Local\\Ankama\\Dofus\\DofusInvoker.swf
FFDEC = $(CURDIR)/FFDec/ffdec.bat
DOFUS_SRC = $(CURDIR)/protocolBuilder/sources
SELECTCLASS = com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++

updateProtocol: decompile gen-protocol gen-msgClasses gen-msgSuffle

decompile:
	@$(FFDEC) -config parallelSpeedUp=0 -selectclass $(SELECTCLASS) -export script $(DOFUS_SRC) $(DOFUSINVOKER)

gen-protocol:
	@python protocolBuilder/protocolParser.py $(DOFUS_SRC)

gen-msgClasses:
	@python protocolBuilder/exportClasses.py

gen-msgShuffle:
	@python protocolBuilder/extractMsgShuffle.py $(DOFUS_SRC)/scripts/com/ankamagames/dofus/network/MessageReceiver.as

deps:
	@pip install -r requirements.txt

startSniffer:
	@python -m snifferApp 

venvActivate:
	@$(CURDIR)/.venv/Scripts/activate.ps1
