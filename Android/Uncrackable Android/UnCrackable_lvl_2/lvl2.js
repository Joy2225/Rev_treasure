Java.perform(function(){
    let c = Java.use("sg.vantagepoint.a.b");
    c["a"].implementation = function () {
        return false
    };

    c["b"].implementation = function () {
        return false;
    };

    c["c"].implementation = function () {
        return false;
    };
})