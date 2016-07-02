var MenuController = function ($scope, $location, $rootScope) {

    // Menu items
    $scope.items = [
        { name: 'Home', icon: 'home', url: '/', active: true },
        { name: 'Camera', icon: 'camera', url: '/camera', active: false },
        { name: 'Recognizer', icon: 'lightning', url: '/recognizer', active: false },
        { name: 'Devices', icon: 'disk outline', url: '/devices', active: false },
        { name: 'Solve', icon: 'cube', url: '/solve', active: false }
    ];

    // Refresh active element
    $scope.refresh = function () {
        var url = $location.url();

        angular.forEach($scope.items, function (item, key) {
            $scope.items[key].active = item.url == url;
        });
    }

    // Redirect function
    $scope.redirect = function (url) {
        $location.path(url);
    }

    // Refresh on route change
    $rootScope.$on('$locationChangeStart', function () {
         $scope.refresh();
    });

    // Refresh on load
    $scope.refresh();
}
