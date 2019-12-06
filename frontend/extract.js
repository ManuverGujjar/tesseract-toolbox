var text = "";
var textArea = document.getElementById("text");

function create(file) {
    var python = require("child_process").spawn("/usr/local/bin/python3", [
        "/Users/manuver/programs/project/tesseract/backend/extractor.py",
        file
    ]);
    python.stdout.on("data", function(data) {
        textArea.innerHTML += data.toString("utf8");
    });
}

file = fileToBeOpen;
$("#extract-start").on("click", function() {
    if (file != undefined) {
        create(file);
    } else {
        alert("please choose a file :)");
    }
});
