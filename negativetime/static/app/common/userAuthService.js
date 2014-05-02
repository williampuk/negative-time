'use strict';

docApp.factory('AuthInterceptor', function ($window, $q) {
    return {
        request: function(config) {
            config.headers = config.headers || {};
            if ($window.sessionStorage.getItem('token')) {
                config.headers.Authorization = 'jwt ' + $window.sessionStorage.getItem('token');
            }
            return config || $q.when(config);
        },
        response: function(response) {
            if (response.status === 401) {
                // TODO: Redirect user to login page.
            }
            return response || $q.when(response);
        }
    };
});

// Register the previously created AuthInterceptor.
docApp.config(function ($httpProvider) {
    $httpProvider.interceptors.push('AuthInterceptor');
});

docApp.factory('userAuthService', ['$http', '$window', function($http, $window) {
	var appUser = undefined;

    var _loadUser = function() {
        if (!appUser) {
            $http.get('/user/').success(function(data) {
                appUser = data;
            })
        }
    }

    _loadUser();

	return {
		isSignedIn: function() {
			return !!appUser;
		},

        getUser: function() {
            return appUser;
        },

		signIn: function(username, password) {
            var user = {
                username: username,
                password: password
            };

            return $http.post('/api-token-auth/', user)
                .success(function (data) {
                    // Stores the token until the user closes the browser window.
                    $window.sessionStorage.setItem('token', data.token);
                    _loadUser();
                })
            .error(function () {
                $window.sessionStorage.removeItem('token');
                // TODO: Show something like "Username or password invalid."
            });

		},

	    logoutUser: function() {
            $window.sessionStorage.removeItem('token');
            appUser = undefined;
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
