'use strict';

docApp.controller('funnyEditorCtrl', ['$scope', '$stateParams', 'projectService', function($scope, $stateParams, projectService) {

    $('#editor1').val(" <h1>Your Funniest Story <br/> <small>This book welcomes all people to fork and share their funniest stories in their daily life.</small> </h1>  <p><br/></p> <h3>Two problems</h3> <p>Some people, when confronted with a problem, think, \"I know, I'll use regular expressions.\" Now they have two problems.</p> ");
    CKEDITOR.replace( 'editor1' );
}]);