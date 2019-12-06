const { dialog } = require("electron").remote;
const fs = require("fs");

function save(contents) {
    dialog.showSaveDialog(function(fileName) {
        if (fileName == undefined) return;

        fs.writeFile(fileName, contents, function(err) {
            if (err)
                alert("Error Occured While Saving the file " + err.message);
        });
    });
}

var textArea = document.getElementById("text");
var saveBtn = document.getElementById("save-btn");
saveBtn.addEventListener("click", function() {
    if (textArea.innerHTML != "") save(textArea.value);
});

var fileToBeOpen = "";
var savePath = "";
function read() {
    fileToBeOpen = "";
    dialog.showOpenDialog(fileName => {
        if (fileName == undefined) return;
        fileToBeOpen += fileName;
        return fileName;
    });
}

function readDir() {
    savePath = "";
    dialog.showOpenDialog({ properties: ["openDirectory"] }, fileName => {
        if (fileName == undefined) return;
        savePath += fileName;
        return fileName;
    });
}

$(".open").on("click", function() {
    read();
});

$("#open-path").on("click", function() {
    readDir();
});

var text = "";
var textArea = document.getElementById("text");

function create(file) {
    textArea.value = "";
    var python = require("child_process").spawn("/usr/local/bin/python3", [
        "/Users/manuver/programs/project/tesseract/backend/extractor.py",
        file
    ]);
    python.stdout.on("data", function(data) {
        textArea.value += data.toString("utf8");
    });
}

$("#extract-start").on("click", function() {
    // alert(fileToBeOpen);
    if (fileToBeOpen != "") {
        create(fileToBeOpen);
        fileToBeOpen = "";
    } else {
        alert("please choose a file :)");
    }
});

fileToRead = "/Users/manuver/programs/project/tesseract/backend/output.txt";
flag = false;
function update() {
    fs.readFile(fileToRead, function(err, data) {
        $("#status-download").html(data.toString());
    });
    setTimeout(function() {
        if (flag) update();
    }, 1000);
}

function download_topics(file, path, sub, no) {
    textArea.innerHTML = "";
    flag = true;
    // let l = alert;
    // l(file);
    // l(path);
    // l(sub);
    // l(no);
    var python = require("child_process").spawn("/usr/local/bin/python3", [
        "/Users/manuver/programs/project/tesseract/backend/Scrapper.py",
        file,
        path,
        sub,
        no
    ]);
    update();
    python.stdout.on("data", function() {
        flag = false;
    });
}

$("#download-start").on("click", function() {
    if (savePath == "") alert("please select data save path");
    else if (fileToBeOpen == "") alert("please select image");
    else {
        download_topics(
            fileToBeOpen,
            savePath,
            document.getElementById("sub").value,
            document.getElementById("not").value
        );
    }
});
