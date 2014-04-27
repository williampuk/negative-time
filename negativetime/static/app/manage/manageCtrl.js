'use strict';

docApp.controller('manageCtrl', ['$scope', 'projects', function($scope, projects) {
	this.projects = projects;
}]);