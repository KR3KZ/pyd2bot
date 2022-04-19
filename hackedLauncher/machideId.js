import crypto from 'crypto';
import child_process from 'child_process';


var osPlatform = process.platform;
var getGuuidCmdPerPltf = {
    darwin: "ioreg -rd1 -c IOPlatformExpertDevice",
    win32: {
        native: "%windir%\\System32",
        mixed: "%windir%\\sysnative\\cmd.exe /c %windir%\\System32"
    }["win32" !== process.platform ? "" : "ia32" === process.arch && process.env.hasOwnProperty("PROCESSOR_ARCHITEW6432") ? "mixed" : "native"] + "\\REG.exe QUERY HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography /v MachineGuid",
    linux: "( cat /var/lib/dbus/machine-id /etc/machine-id 2> /dev/null || hostname ) | head -n 1 || :",
    freebsd: "kenv -q smbios.system.uuid || sysctl -n kern.hostuuid"
};

function hashWithSha256(str) {
    return crypto.createHash("sha256").update(str).digest("hex");
}

function parseMachineGuuidFromCmdStdOut(stdOut) {
    switch (process.platform) {
        case "darwin":
            return stdOut.split("IOPlatformUUID")[1].split("\n")[0].replace(/\=|\s+|\"/gi, "").toLowerCase();
        case "win32":
            return stdOut.toString().split("REG_SZ")[1].replace(/\r+|\n+|\s+/gi, "").toLowerCase();
        case "linux":
        case "freebsd":
            return stdOut.toString().replace(/\r+|\n+|\s+/gi, "").toLowerCase();
        default:
            throw new Error("Unsupported platform: " + process.platform);
    }
}

export function machineIdSync(withSha256Hash) {
    var machineGuuid = parseMachineGuuidFromCmdStdOut(child_process.execSync(getGuuidCmdPerPltf[osPlatform]).toString());
    return withSha256Hash ? machineGuuid : hashWithSha256(machineGuuid);
}

export function machineId(withSha256Hash) {
    return child_process.exec(getGuuidCmdPerPltf[osPlatform], (err, stdout, stderr) => {
        if (err)
            return console.log(new Error("Error while obtaining machine id: " + err.stack));
        var machineGuuid = parseMachineGuuidFromCmdStdOut(stdout.toString());
        return withSha256Hash ? machineGuuid : hashWithSha256(machineGuuid)
    })
}


