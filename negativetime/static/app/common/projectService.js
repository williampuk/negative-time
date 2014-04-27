'use strict';

docApp.factory('projectService', ['$http', function($http) {
	// var Project = $http.get('/projects/');

	var projects = undefined;

	return {
		getProjects : function() {
			return $http.get('/projects/').then(function(response) {
                projects = response.data;
				return response.data;
			});
		},

        getCachedProjects : function() {
            return projects;
        }
	};
	
}]);