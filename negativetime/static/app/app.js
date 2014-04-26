'use strict';

var docApp = angular.module('docApp', ['ui.bootstrap', 'ui.router', 'ngResource', 'ngCookies']);


docApp.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

  $urlRouterProvider.otherwise("/discover");

  //Home State
  $stateProvider
    .state('discover', {
      url: "/discover",
      templateUrl: "discover/discover.html"
    })

    .state('create', {
      url: "/create",
      templateUrl: "create/create.html"
    })

    // SignIn State
    .state('signIn', {
      url: "/signIn",
      templateUrl: "signIn/signIn.html",
      controller: 'signInCtrl as signIn'
    });

}])
.run(['$http', '$cookies', function($http, $cookies) {
	console.log('csrftoken', $cookies.csrftoken);
	$http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
}]);
// .run(['$state', '$rootScope', function($state, $rootScope) {
// 	$rootScope.$state = $state;
// 	console.log('state', $rootScope.$state);
// }]);