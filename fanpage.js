var page = require('webpage').create();
// open the required page in PhantomJS
page.settings.userAgent = 'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54';

page.onLoadFinished = function(status){
    var allImgSrc = page.evaluate(function(){
        return [].map.call(document.querySelectorAll('img'),function(img){
            return img.getAttribute('src');
        });
    });
    console.log(allImgSrc.join('\n'));
    phantom.exit();
};

page.onConsoleMessage = function (message){
    console.log("msg: " + message);
};

page.open('http://www.facebook.com/plugins/fan.php?connections=100&id=132769576762243');
