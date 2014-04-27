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

    .state('manage', {
      url: "/manage",
      templateUrl: "manage/manage.html",
      controller: 'manageCtrl as manage',
      resolve: {
        projects: ['projectService', function(projectService) {
          return projectService.getProjects();
        }]
      }
    })

    .state('editor', {
      url: "/editor/:index",
      templateUrl: "editor/editor.html",
      controller: 'editorCtrl'
    })

    .state('funnystory', {
        url: "/funnystory",
        templateUrl: "funnystory/funnystory.html",
    })

    .state('funnystoryeditor', {
        url: "/funnystoryeditor/",
        templateUrl: "funnystoryeditor/editor.html",
        controller: 'funnyEditorCtrl'
    })

    .state('funnystoryedited', {
        url: "/funnystoryedited/",
        templateUrl: "funnystoryedited/funnystory.html",
    })
    // SignIn State
    .state('signIn', {
      url: "/signIn",
      templateUrl: "signIn/signIn.html",
      controller: 'signInCtrl as signIn'
    });

}])
.run(['$http', '$cookies', '$rootScope', '$state', function($http, $cookies, $rootScope, $state) {
  // $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;

  $http.get('/admin/').then( function() {
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  });
  
  $rootScope.$on('$stateChangeError', function(event, toState, toParams, fromState, fromParams, error){
    $state.go('signIn');
  });
}]);
// .run(['$state', '$rootScope', function($state, $rootScope) {
// 	$rootScope.$state = $state;
// 	console.log('state', $rootScope.$state);
// }]);