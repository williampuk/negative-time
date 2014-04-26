'use strict';

docApp.controller('navBarCtrl', ['$scope', 'userAuthService', function($scope, userAuthService) {

	$scope.isSignedIn = function() {
		return userAuthService.isSignedIn();
	}

	$scope.username = userAuthService.getUser() ? userAuthService.getUser().username : '';

}])