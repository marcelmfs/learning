//
// If invoked with "-v" it will print out the Page Resources as they are
// Requested and Received.
//
// NOTE.1: The "onConsoleMessage/onAlert/onPrompt/onConfirm" events are
// registered but not used here. This is left for you to have fun with.

var sys = require("system"),
    page = require("webpage").create(),
    logResources = false;

page.settings.userAgent = 'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54';

if (sys.args.length > 1 && sys.args[1] === "-v") {
    logResources = true;
} else {
    var pageName = sys.args[1];
    console.log(sys.args[1]);
}

function printArgs() {
    var i, ilen;
    for (i = 0, ilen = arguments.length; i < ilen; ++i) {
        console.log("    arguments[" + i + "] = " + JSON.stringify(arguments[i]));
    }
    console.log("");
}

////////////////////////////////////////////////////////////////////////////////

page.onInitialized = function() {
    console.log("page.onInitialized");
    printArgs.apply(this, arguments);
};
page.onLoadStarted = function() {
    console.log("page.onLoadStarted");
    printArgs.apply(this, arguments);
};
page.onLoadFinished = function() {
    console.log("page.onLoadFinished");
    printArgs.apply(this, arguments);
};
page.onUrlChanged = function() {
    console.log("page.onUrlChanged");
    printArgs.apply(this, arguments);
};
page.onNavigationRequested = function() {
    console.log("page.onNavigationRequested");
    printArgs.apply(this, arguments);
};
page.onRepaintRequested = function() {
    console.log("page.onRepaintRequested");
    printArgs.apply(this, arguments);
};

if (logResources === true) {
    page.onResourceRequested = function() {
        console.log("page.onResourceRequested");
        printArgs.apply(this, arguments);
    };
    page.onResourceReceived = function() {
        console.log("page.onResourceReceived");
        printArgs.apply(this, arguments);
    };
}

// window.onClosing()
page.onClosing = function() {
    console.log("page.onClosing");
    printArgs.apply(this, arguments);
};

// window.console.log(msg);
page.onConsoleMessage = function() {
    console.log("page.onConsoleMessage");
    printArgs.apply(this, arguments);
};

// window.alert(msg);
page.onAlert = function() {
    console.log("page.onAlert");
    printArgs.apply(this, arguments);
};
// var confirmed = window.confirm(msg);
page.onConfirm = function() {
    console.log("page.onConfirm");
    printArgs.apply(this, arguments);
};
// var user_value = window.prompt(msg, default_value);
page.onPrompt = function() {
    console.log("page.onPrompt");
    printArgs.apply(this, arguments);
};

////////////////////////////////////////////////////////////////////////////////

function doLogin(){
    page.evaluate(function(){
        var frm = document.getElementById("login_form");
        frm.elements["email"].value = "beata.revoltada";
        frm.elements["pass"].value = "S3nh45";
        frm.submit();
    });
    page.open("http://graph.facebook.com/"+pageName);
}

function doUpdateStatus(){
    page.evaluate(function(){
        var form = document.getElementById("composer_form");
        form.elements["status"].value = new Date().toString()+" Outro teste status update.";
        form.submit();
    });
}

function doCrawlPage(){
    page.evaluate(function(){
        var users = 
    });
}

page.onLoadFinished = function(status){
    console.log( (!phantom.state ? "no-state" : phantom.state) + ": " + status );
    if(status === "success"){
        if( !phantom.state ){
            doLogin();
            phantom.state = "logged-in";
        } else if(phantom.state === "logged-in"){
            //doUpdateStatus();
            doCrawlPage();
            //phantom.state = "status-updated";
        } else if(phantom.state === "status-updated"){
            phantom.exit();
        }
    }
};

page.onConsoleMessage = function (message){
    console.log("msg: " + message);
};

page.open("https://m.facebook.com");
