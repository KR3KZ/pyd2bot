import { AuthHelper } from "./authHelper.js";

var ah = new AuthHelper();
var login = process.argv[2];
var r = ah.getStoredCertificate(login);
let certhash = ah.generateHashFromCertif(r.certificate);
let ret = {
    id: r.certificate.id,
    hash: certhash
}
console.log(JSON.stringify(ret));