const { app, BrowserWindow } = require("electron");
const path = require("path");
const l = console.log;

function createWindow() {
    let win = new BrowserWindow({
        maxWidth: 1000,
        minWidth: 1000,
        minHeight: 750,
        height: 750,
        width: 1000,
        maxHeight: 750,
        webPreferences: { nodeIntegration: true }
    });
    win.loadFile(path.join(__dirname, "..", "frontend", "index.html"));
    // win.webContents.openDevTools();
}

app.on("ready", function() {
    createWindow();
});
