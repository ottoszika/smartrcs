var app = angular.module('smartrcs', ['ngRoute', 'ngSanitize', 'ng-sortable']);

// Routes
app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'views/home.html',
        controller: HomeController
    }).when('/camera', {
        templateUrl: 'views/camera.html',
        controller: CameraController
    }).when('/recognizer', {
        templateUrl: 'views/recognizer.html',
        controller: RecognizerController
    }).otherwise('/');
});

// Services
app.factory('CameraService', CameraService);
app.factory('RecognizerService', RecognizerService);

// Controllers
app.controller('MenuController', MenuController);

// Directives
app.directive('facelet', FaceletDirective);
