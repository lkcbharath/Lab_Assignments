function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function startTime() {
    var today = new Date();
    var h1 = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var am_pm;
    if(h1==12){
        h = 12;
        am_pm = "PM";
    }
    else if (h1>12){
        h = h1 - 12;
        am_pm = "PM";
    }
    else {
        h = h1;
        am_pm = "AM";
    }
    // add a zero in front of numbers<10
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML = h + ":" + m + ":" + s + " " + am_pm;
    t = setTimeout(function() {
        startTime()
    }, 500);
}

startTime();
  