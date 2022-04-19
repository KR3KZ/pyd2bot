import os
from subprocess import Popen, PIPE
import json
import httpx

from hackedLauncher.CredsManager import CredsManager


class Haapi:
    def __init__(self) -> None:
        self.url = "https://haapi.ankama.com"
        self.APIKEY = None

    def getUrl(self, request):
        return (
            self.url
            + {
                "CREATE_API_KEY": "/json/Ankama/v5/Api/CreateApiKey",
                "GET_LOGIN_TOKEN": "/json/Ankama/v5/Account/CreateToken",
            }[request]
        )

    def createAPIKEY(self, accountId, game_id=102) -> str:
        creds = CredsManager.getEntry(accountId)
        cert = self.getCert(creds["login"])
        data = {
            "login": creds["login"],
            "password": creds["password"],
            "game_id": game_id,
            "long_life_token": True,
            "certificate_id": cert["id"],
            "certificate_hash": cert["hash"],
            "shop_key": "ZAAP",
            "payment_mode": "OK",
        }
        response = httpx.post(
            self.getUrl("CREATE_API_KEY"),
            data=data,
            headers={
                "User-Agent": "Zaap",
                "Content-Type": "multipart/form-data",
            },
        )
        self.APIKEY = response.json()["key"]
        return self.APIKEY

    def getCert(self, login):
        CURRDIR = os.path.dirname(__file__)
        p = Popen(
            ["cd", CURRDIR, "&&", "node", "getCertificate.js", login], stderr=PIPE, stdout=PIPE, shell=True
        )
        stdout, stderr = p.communicate()
        if stderr:
            raise Exception(stderr.decode("utf-8"))
        ret_json = stdout.decode("utf-8")
        cert = json.loads(ret_json)
        return cert

    def getLoginToken(self, accountId, game_id=1):
        if not self.APIKEY:
            self.createAPIKEY(accountId)
        creds = CredsManager.getEntry(accountId)
        cert = self.getCert(creds["login"])
        response = httpx.get(
            self.getUrl("GET_LOGIN_TOKEN"),
            params={
                "game": game_id,
                "certificate_id": cert["id"],
                "certificate_hash": cert["hash"],
            },
            headers={
                "User-Agent": "Zaap",
                "Content-Type": "multipart/form-data",
                "APIKEY": self.APIKEY,
            },
        )
        token = response.json()["token"]
        return token


if __name__ == "__main__":
    myAccountId = "149512160"
    haapi = Haapi()
    print("LOGIN Token " + haapi.getLoginToken(myAccountId))
