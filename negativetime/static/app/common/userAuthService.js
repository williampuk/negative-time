'use strict';

docApp.factory('userAuthService', ['$http', function($http) {
	var appUser = undefined;

	return {
		isLoggedIn: function() {
			return !!appUser;
		},

		signIn: function(username, password) {
			return $http.post('/api-auth/login/', {username:username, password:password}).success(function(data, status, headers, config) {
				console.log(data, status, headers, config);
				appUser = {username: username};
			});
		},

	    logoutUser: function() {
			return $http.get('/api-auth/logout/').success(function(data, status, headers, config) {
				appUser = undefined;
			});
	    }
	};
}]);

    // createUser: function(newUserData) {
    //   var newUser = new mvUser(newUserData);
    //   var dfd = $q.defer();

    //   newUser.$save().then(function() {
    //     mvIdentity.currentUser = newUser;
    //     dfd.resolve();
    //   }, function(response) {
    //     dfd.reject(response.data.reason);
    //   });

    //   return dfd.promise;
    // },

    // updateCurrentUser: function(newUserData) {
    //   var dfd = $q.defer();

    //   var clone = angular.copy(mvIdentity.currentUser);
    //   angular.extend(clone, newUserData);
    //   clone.$update().then(function() {
    //     mvIdentity.currentUser = clone;
    //     dfd.resolve();
    //   }, function(response) {
    //     dfd.reject(response.data.reason);
    //   });
    //   return dfd.promise;
    // },

    // authorizeCurrentUserForRoute: function(role) {
    //   if(mvIdentity.isAuthorized(role)) {
    //     return true;
    //   } else {
    //     return $q.reject('not authorized');
    //   }

    // },
    // authorizeAuthenticatedUserForRoute: function() {
    //   if(mvIdentity.isAuthenticated()) {
    //     return true;
    //   } else {
    //     return $q.reject('not authorized');
    //   }
    // }
