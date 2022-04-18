from com.ankamagames.dofus.logic.connection.managers.AuthentificationManager import (
    AuthentificationManager,
)
from com.ankamagames.dofus.logic.shield.SecureModeManager import SecureModeManager


AuthentificationManager().setCredentials("kmajdoub", "sdgsdfsf")
cert = SecureModeManager().retreiveCertificate()
print(cert)
print()
