'use strict';

docApp.directive('onEnterKeyDown', function() {
	return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.onEnterKeyDown);
                });
                event.preventDefault();
            }
        });
    };
});

//docApp.directive('richTextEditor', function() {
//    return {
//        link : function(scope, element, attrs, ctrl) {
//            element.wysiwyg();
//        }
//    };
//});
