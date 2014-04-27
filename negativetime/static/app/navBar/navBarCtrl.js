'use strict';

docApp.controller('navBarCtrl', ['$scope', 'userAuthService', function($scope, userAuthService) {

	$scope.isSignedIn = function() {
		$scope.username = userAuthService.getUser() ? userAuthService.getUser().username : '';
		return userAuthService.isSignedIn();
	};

}])