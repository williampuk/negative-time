'use strict';

docApp.controller('editorCtrl', ['$scope', '$stateParams', 'projectService', function($scope, $stateParams, projectService) {

    $scope.project = projectService.getCachedProjects()[$stateParams.index]

    CKEDITOR.replace( 'editor1' );

}]);