var cvs;
var ctx;
var drawing = false;
var x;
var y;

window.addEventListener("load", init, false);

function init(ev) {
    cvs = document.getElementById("canvas1");
    ctx = cvs.getContext("2d");
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctx.lineWidth = 5;
    ctx.fillStype = "#3f3f3f";
    cvs.addEventListener("mousedown", start, false);
    cvs.addEventListener("mousemove", move, false);
    cvs.addEventListener("mouseup", stop, false);
    cvs.addEventListener("touchstart", start_touch, false);
    cvs.addEventListener("touchmove", move_touch, false);
    cvs.addEventListener("touchend", stop_touch, false);
}
function start(ev) {
    x = ev.layerX;
    y = ev.layerY;
    ctx.beginPath();
    ctx.moveTo(x,y);
    drawing = true;
}
function move(ev) {
    if ( drawing ) {
        x = ev.layerX;
        y = ev.layerY;
        ctx.lineTo(x,y);
        ctx.stroke();
    }
}
function stop(ev) {
    ctx.closePath();
    drawing = false;
    document.getElementById("button1").value = cvs.toDataURL("image/png");
}
function start_touch(ev) {
    x = ev.changedTouches[0].pageX;
    y = ev.changedTouches[0].pageY;
    ctx.beginPath();
    ctx.moveTo(x,y);
    drawing = true;
}
function move_touch(ev) {
    if ( drawing ) {
        x = ev.changedTouches[0].pageX;
        y = ev.changedTouches[0].pageY;
        ctx.lineTo(x,y);
        ctx.stroke();
    }
}
function stop_touch(ev) {
    ctx.closePath();
    drawing = false;
    document.getElementById("button1").value = cvs.toDataURL("image/png");
}
