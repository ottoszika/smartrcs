var RecognizerService = function ($http) {

    // Common url
    var url = '/api/recognizer';

    // Will returned to export all properties
    var service = { };

    // Get configuration from server
    service.getConfiguration = function (cb) {

        // Make a GET request to API
        $http({
            method: 'GET',
            url: url + '?type=json'
        }).then(function (response) {

            // Callback
            cb(response.data);
        });
    };

    // Get snapshot from server
    service.getSnapshot = function (cb) {

        // Make a GET request to API
        $http({
            method: 'GET',
            url: url + '?type=img'
        }).then(function (response) {

            // Callback
            cb(response.data);
        });
    };

    // Post configuration to server
    service.postConfiguration = function (data, cb) {

        // Make a GET request to API
        $http({
            method: 'POST',
            url: url,
            data: data
        }).then(function (response) {

            // Callback
            cb(response.data);
        });
    };

    return service;
};
