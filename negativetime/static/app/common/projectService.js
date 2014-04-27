'use strict';

docApp.factory('projectService', ['$http', function($http) {
	// var Project = $http.get('/projects/');

	// console.log(Project);

	return {
		getProjects : function() {
			return $http.get('/projects/').then(function(response) {
				return response.data;
			});
		}
	};
	
}]);