'use strict';

docApp.controller('signInCtrl', ['$scope', 'userAuthService', '$state', function($scope, userAuthService, $state) {
	
	this.signIn = function() {
		userAuthService.signIn(this.username, this.password).success( function() {
			console.log('success!');
			$state.go('discover');
		});
	};
}]);