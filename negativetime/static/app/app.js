'use strict';

var docApp = angular.module('docApp', ['ui.bootstrap', 'ui.router']);


docApp.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

  $urlRouterProvider.otherwise("/discover");

  //Home State
  $stateProvider
    .state('discover', {
      url: "/discover",
      templateUrl: "discover/discover.html"
    })
    // SignIn State
    .state('signIn', {
      url: "/signIn",
      templateUrl: "signIn/signIn.html",
      controller: 'signInCtrl'
    });

}]);

docApp.run(['$state', '$rootScope', function($state, $rootScope) {
	$rootScope.$state = $state;
	console.log('state', $rootScope.$state);
}]);