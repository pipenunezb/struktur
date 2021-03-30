$(document).ready(function(){
    if($("body").height() < $(window).height()){
        $("footer").css({"position":"absolute","bottom":"0px"});
        $("body").css({"height":$(window).height()});
    }
});