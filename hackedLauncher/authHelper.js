import { DeviceSpecs } from './deviceSpecs.js';
import path from 'path';
import { App } from './app.js';
import * as fs from 'fs';
import { CryptoHelper } from './cryptoHelper.js';
import { machineIdSync } from './machideId.js';
import os from 'os';


export class AuthHelper {

    constructor() {
        this.cryptoHelper = new CryptoHelper();
    }

    getApiKeysFolderPath() {
        return path.join(App.getPath("userData"), "keydata")
    }

    getStoredCertificate(username) {
        const certFolder = this.getCertificateFolderPath()
        var certPath = path.join(certFolder, `.certif${this.cryptoHelper.createHashFromStringSha(username)}`);
        if (fs.existsSync(certPath))
            try {
                return {
                    certificate: this.cryptoHelper.decryptFromFileWithUUID(certPath),
                    filepath: certPath
                }
            } catch (e) {
                console.log(`[1020 AUTH_HELPER] delete indecipherable certificate on ${certPath}`, e);
                try {
                    fs.unlinkSync(certPath)
                } catch (e) {
                    console.log(`[1030 AUTH_HELPER] Impossible to delete certificate file : ${e.message}`)
                }
            }
        return Promise.resolve(null)
    }

    generateApiForAccount(username, t, n) {
        return this.getStoredCertificate(username).then(async r => {
            if (r) {
                const {
                    certificate: certificate,
                    filepath: filepath
                } = r;
                let certHash;
                try {
                    certHash = this.generateHashFromCertif(certificate)
                } catch (r) {
                    s.error(`[1022 AUTH_HELPER] Error on generateHashFromCertif, \n ${r} \n delete certificate on ${filepath}`);
                    try {
                        fs.unlinkSync(filepath)
                    } catch (e) {
                        s.warn(`[1032 AUTH_HELPER] Impossible to delete certificate file : ${e.message}`)
                    }
                    return this.Haapi.instance.get("ankama.api.createApiKey", username, t, n).then(e => e)
                }
                const certId = certificate.id;
                return this.Haapi.instance.get("ankama.api.createApiKey", username, t, n, certId, certHash).then(e => (e.certificate = certificate, e))
            }
            return this.Haapi.instance.get("ankama.api.createApiKey", username, t, n).then(e => e)
        })
    }

    generateHashFromCertif(cert) {
        const {
            hm1: hashedMachineInfos,
            hm2: hashedMachineInfos_reversed
        } = this.createHmEncoders();
        return this.cryptoHelper.generateHashFromCertif(cert, hashedMachineInfos, hashedMachineInfos_reversed)
    }

    getCertificateFolderPath() {
        return path.join(App.getPath("userData"), 'certificate');
    }

    createHmEncoders() {
        const devicespecs = DeviceSpecs.instance;
        let data = [];
        data.push(os.arch());
        data.push(os.platform());
        data.push(machineIdSync());
        data.push(os.userInfo().username);
        data.push(devicespecs.getOsVersion());
        data.push(devicespecs.getComputerRam());
        let machineInfos = data.join("");
        const hashedMachineInfos = this.cryptoHelper.createHashFromStringSha(machineInfos);
        let hashedMachineInfos_reversed = hashedMachineInfos.split("").reverse().join("");
        return {
            hm1: hashedMachineInfos,
            hm2: hashedMachineInfos_reversed
        }
    }
}
