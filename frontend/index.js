// let $ = require("jquery");

var download = $("#downloader");
var extract = $("#extractor");

function changeNav(t) {
    let links = document.getElementsByClassName("nav-link");
    if (t === links[1]) {
        links[1].classList.add("active");
        links[0].classList.remove("active");
        download.hide();
        extract.show();
    } else {
        links[0].classList.add("active");
        links[1].classList.remove("active");
        extract.hide();
        download.show();
    }
}
