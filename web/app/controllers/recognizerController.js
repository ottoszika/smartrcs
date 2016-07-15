var RecognizerController = function ($scope, RecognizerService) {

    // Configuration model
    $scope.config = { };

    // Rotation knob options
    $scope.knobOptions = {
        width: 48,
        height: 48,
        min: 0,
        max: 360,
        step: 90,
        cursor: true,
        bgColor: '#eee',
        fgColor: '#000',
        thickness: 0.3,
        lineCap: 'round'
    };

    $scope.sortableConfig = {
        ghostClass: 'order-item-ghost',
        chosenClass: 'order-item-chosen'
    }

    // Facelet colors
    $scope.selectCubie = ['#fff', '#fff', '#fff',
                          '#fff', '#fff', '#fff',
                          '#fff', '#fff', '#fff'];

    // Facelet texts
    $scope.textCubie = ['', '', '',
                        '', '', '',
                        '', '', ''];

    // Current cubie on facelet
    $scope.currentAutoButton = -1;

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
        RecognizerService.postConfiguration($scope.config, function (data) {

            // Show saving result
            $scope.saver = { active: true, success: !data.error };
            $scope.resetSaveDimmer();

            $scope.loader = { active: false, message: null };
        });
    };

    // Get configuration data and store in model
    $scope.load = function () {
        $scope.loader = { active: true, message: 'Loading...' };
        RecognizerService.getConfiguration(function (data) {
            $scope.config = data;
            $scope.loader = { active: false, message: null };
        });
    }

    // Get click position within the image and modify the model
    $scope.selectImage = function ($event) {
        var x = $event.offsetX * $event.target.naturalWidth / $event.target.clientWidth;
        var y = $event.offsetY * $event.target.naturalHeight / $event.target.clientHeight;

        x = parseInt(x);
        y = parseInt(y);

        $scope.config.facelet[$scope.currentAutoButton][0] = x;
        $scope.config.facelet[$scope.currentAutoButton][1] = y;
        $scope.textCubie[$scope.currentAutoButton] = 'x: ' + x + '<br /> y: ' + y;

        $scope.nextAuto();
    };

    // Next cubie
    $scope.nextAuto = function () {
        if ($scope.currentAutoButton >= 9) {
            return ;
        }

        $scope.currentAutoButton++;

        angular.forEach($scope.selectCubie, function (value, key) {
            if (key == $scope.currentAutoButton) {
                $scope.selectCubie[key] = '#ccc';
            } else {
                $scope.selectCubie[key] = '#fff';
            }
        })
    };

    // Reset all to server values and defaults
    $scope.reset = function () {
        $scope.currentAutoButton = -1;

        $scope.selectCubie = ['#fff', '#fff', '#fff',
                          '#fff', '#fff', '#fff',
                          '#fff', '#fff', '#fff'];

        $scope.textCubie = ['', '', '',
                            '', '', '',
                            '', '', ''];

        $scope.nextAuto();
        $scope.load();
    };

    // Initialize stuffs
    $scope.load();
    $('#recognizer-tab .item').tab();
    $scope.nextAuto();
};
