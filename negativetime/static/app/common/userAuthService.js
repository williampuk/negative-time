'use strict';

docApp.factory('userAuthService', ['$http', function($http) {
	var appUser = undefined;

	return {
		isLoggedIn: function() {
			return !!appUser;
		},

		signIn: function(username, password) {

			var defaultsHeader = angular.extend({}, $http.defaults.headers);

			var config = {
				method: 'POST',
				url: '/login/',
				data: $.param({username:username, password:password}),
				headers: angular.extend(defaultsHeader, {'Content-Type' : 'application/x-www-form-urlencoded'})
			};

			return $http(config).success(function(data, status, headers, config) {
				console.log(data, status, headers, config);
				appUser = {username: username};
			});
		},

	    logoutUser: function() {
			return $http.get('/logout/').success(function(data, status, headers, config) {
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
