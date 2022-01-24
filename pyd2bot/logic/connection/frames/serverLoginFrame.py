import pyd2bot.bot as bot
from pyd2bot.logic.connection.managers import AuthentificationManager
import math
import random
from pyd2bot.utils.crypto import RSA, RSACipher, PKCS1
from pyd2bot.utils.binaryIO import ByteArray


class ServerLoginFrame:

    def __init__(self, client):
        self.client = client    
        
    def handleConnectionOpened(self):
        pass
    
    def handleConnectionClosed(self):
        pass
      
    def process(self, msg) -> bool:
        mtype = msg["__type__"]
        
        if mtype == "ServersListMessage":
            self.client.send({
                '__type__': 'ServerSelectionMessage',
                'serverId': bot.Bot.serverID
            })
            return True
        
        elif mtype == "SelectedServerDataMessage":
            self.client.serverInfos = msg
            ba_ticket = AuthentificationManager.decodeWithAES(msg["ticket"])
            self.client.serverInfos["ticket"] = ba_ticket.decode()
            self.client.game_server_host = msg["address"]
            self.client.sock.close()
            self.counter = 0
            self.client.connectToGameServer()
            return True
        
        elif mtype == "HelloGameMessage":
            ticketMsg = {
                '__type__': 'AuthenticationTicketMessage',
                'lang': 'fr',
                'ticket': self.client.serverInfos["ticket"]
            }
            self.client.send(ticketMsg)
            return True
        
        elif mtype == "RawDataMessage":
            # Bypass humain check here
            gameServerTicket = self.client.serverInfos["ticket"]

            key = b"AKMBJ2YBJUHRsk8yptfOlcVLksJSCCSiWUryWD/vv6euIERWlfrWN0+Csf8UVG4CY"\
                b"qoz3hDBuaA3oe48W1xFADd5Bm+ks0dW3hemrTSI7HBLSLBWAcKrZ21wPfgWD2QUxVV1infGd"\
                b"pw+Lt0808UwqdDGUpwV2JGqzIbMZjGCXWdj8Ae2ribiXWU2P255Uv5nhC7O4ZKoTNXDAmjtc"\
                b"3qYzSXUZTkrhlf3yL8J/XyUvHuvuKetABtoJun2QaaKkuO6258oDtDxnKQKgKhtVrc0Jpa"\
                b"Qusr7GlWRcg6bK2M8dWjj+TAuwZLMvn7ltKYJjgvYymasrRu+56wbreTHa98ctVE="
                
            publicModulo = int.from_bytes(key, "big")
            rsaKeyNetwork = RSA.RsaKey(n=publicModulo, e=65537) 

            keyLen = 128
            hashKey = bytearray()
            i = 0
            while i < keyLen // 8:
                rb = math.floor(random.random() * 256) - 128
                hashKey += rb.to_bytes(1, "big", signed=True)
                i+=1
                
            xorKey2Len = math.floor(random.random() * 128) + 128
            xorKey2 = bytearray()
            i = 0
            while(i < xorKey2Len // 8):
                rb =  math.floor(random.random() * 256 - 128)
                xorKey2 += rb.to_bytes(1, "big", signed=True)
                i+=1 
            i = 0

            dataToEncrypt = ByteArray()
            dataToEncrypt.writeUTF(gameServerTicket)
            dataToEncrypt.writeShort(len(hashKey))
            dataToEncrypt += hashKey
            dataToEncrypt.writeShort(len(xorKey2))
            dataToEncrypt += xorKey2
            dataToEncrypt.position = 0

            dataIndex = 0
            while dataIndex < len(dataToEncrypt):
                dataToEncrypt[dataIndex] = 0 ^ 0
                dataIndex += 1

            rsacipher = RSACipher(rsaKeyNetwork, PKCS1())
            enc_data = rsacipher.encrypt(dataToEncrypt)
            ret = enc_data.to_int8Arr()
            self.client.send({
                '__type__': 'CheckIntegrityMessage',
                'data': ret
            })
            return True
            
        elif mtype == "TrustStatusMessage":
            bot.Bot.connected.set()
            self.client.send({'__type__': 'CharactersListRequestMessage'})
            return True

        elif mtype == "CharactersListMessage":
            for character in msg["characters"]:
                if character["name"] == bot.Bot.characterName:
                    bot.Bot.characterID = character["id"]
            self.client.send({
                '__type__': 'CharacterSelectionMessage', 
                'id': bot.Bot.characterID
            })
            return True

        
