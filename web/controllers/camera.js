var CameraController = function ($scope, CameraService) {

    // Configuration model
    $scope.config = { };

    // Loader and saver
    $scope.loader = { active: false, message: null };
    $scope.saver = { active: false, success: null };

    // Clear save dimmer
    $scope.resetSaveDimmer = function () {

        // Reset after 800ms
        setTimeout(function () {
            $scope.saver = { active: false, success: null };
            $scope.$apply();
        }, 800);
    }

    // Post configuration data from model
    $scope.save = function () {
        $scope.loader = { active: true, message: 'Saving...' };
        CameraService.postConfiguration($scope.config, function (data) {

            // Show saving result
            $scope.saver = { active: true, success: !data.error };
            $scope.resetSaveDimmer();

            $scope.loader = { active: false, message: null };
        });
    }

    // Get configuration data and store in model
    $scope.loader = { active: true, message: 'Loading...' };
    CameraService.getConfiguration(function (data) {
        $scope.config = data;
        $scope.loader = { active: false, message: null };
    });
}
