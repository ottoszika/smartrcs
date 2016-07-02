var app = angular.module('smartrcs', ['ngRoute']);

app.controller('MenuController', MenuController);

app.config(function ($routeProvider) {
    $routeProvider.when('/camera', {
        templateUrl: 'views/camera.html',
        controller: CameraController
        }
    );
});

app.factory('CameraService', CameraService);
