import path from 'path';

export class App {

    static getPath(flag) {
        if (flag == "userData") {
            return path.join(process.env.AppData, 'zaap')
        }
    }
}