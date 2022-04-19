// depends on os, crypto, fs
import os from 'os';
import crypto from 'crypto';
import fs from 'fs';
import { machineIdSync } from './machideId.js';

export class CryptoHelper {

    getUUID() {
        return [os.platform(), os.arch(), machineIdSync(), os.cpus().length, os.cpus()[0].model].join()
    }

    createHashFromString(str) {
        var md5Hasher = crypto.createHash("md5");
        var hash = md5Hasher.update(str);
        return hash.digest();
    }

    createHashFromStringSha(str) {
        var sha256Hasher = crypto.createHash("sha256");
        var hash = sha256Hasher.update(str);
        return hash.digest('hex').slice(0, 32);
    }

    encrypt(json, t) {
        var key = this.createHashFromString(t);
        var iv = crypto.randomBytes(16);
        var cipher = crypto.createCipheriv("aes-128-cbc", key, iv);
        var o = Buffer.from(JSON.stringify(json), "utf8");
        var a = Buffer.concat([s.update(o), cipher.final()]);
        return iv.toString("hex") + "|" + a.toString("hex")
    }

    generateHashFromCertif(cert, hashedMachineInfos, hashedMachineInfos_reversed) {
        let cipher = crypto.createDecipheriv("aes-256-ecb", hashedMachineInfos_reversed, "");
        let s = Buffer.concat([cipher.update(cert.encodedCertificate, "base64"), cipher.final()]);
        return crypto.createHash("sha256").update(hashedMachineInfos + s.toString()).digest("hex");
    }

    decryptFromFileWithUUID(filePath) {
        const uuid = this.getUUID();
        return this.decryptFromFile(filePath, uuid);
    }

    decryptFromFile(filePath, uuid) {
        let data = fs.readFileSync(filePath, "utf8")
        try {
            return this.decrypt(data, uuid);
        } catch (err) {
            console.log("[1019 CRYPTO_HELPER] cannot decrypt from file", filePath, err);
            throw err;
        }
    }

    decrypt(data, uuid) {
        var r = data.split("|");
        var iv = Buffer.from(r[0], "hex");
        var dataToDecrypt = Buffer.from(r[1], "hex");
        var key = this.createHashFromString(uuid);
        var decipher = crypto.createDecipheriv("aes-128-cbc", key, iv);
        var plainText = decipher.update(dataToDecrypt);
        var u = Buffer.concat([plainText, decipher.final()]).toString();
        var r = JSON.parse(u);
        return r;
    }
}
