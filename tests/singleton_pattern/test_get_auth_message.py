from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import AuthentificationManager

key = 
AuthentificationManager().setPublicKey(hcmsg.key)
AuthentificationManager().setSalt(hcmsg.salt)
AuthentificationManager().initAESKey()
iMsg = AuthentificationManager().getIdentificationMessage()