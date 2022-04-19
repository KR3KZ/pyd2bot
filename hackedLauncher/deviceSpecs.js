import os from 'os';

export class DeviceSpecs {

    static get instance() {
        return DeviceSpecs._instance || (DeviceSpecs._instance = new DeviceSpecs), DeviceSpecs._instance
    }

    constructor() {
    }

    getComputerRam() {
        return Math.pow(2, Math.round(Math.log(os.totalmem() / 1024 / 1024) / Math.log(2)))
    }

    getOsVersion() {
        var t, n;
        [t, n] = os.release().split(".");
        return parseFloat(`${t}.${n}`)
    }

    // async getCpuSpecs() {
    //     const {
    //         os: e,
    //         logger: t
    //     } = this.dependencies;
    //     try {
    //         const t = os.cpus();
    //         n = [];
    //         n.push(t.length);
    //         n.push(t[0].model);
    //         n.push(t[0].speed);
    //         return t[0], n;
    //     } catch (e) {
    //         console.log.warn("[KPI] Unable to get CPU specs", e)
    //     }
    // }

    // async getGpuSpecs() {
    //     const {
    //         appElectron: e,
    //         logger: t
    //     } = this.dependencies;
    //     try {
    //         return [(await e.getGPUInfo("complete")).auxAttributes.glRenderer]
    //     } catch (e) {
    //         t.warn("[KPI] Unable to get GPU specs", e)
    //     }
    // }
}
