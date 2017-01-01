angular.module("app").service('ServerCommunication', function(AppConfig, $http){
    // TODO: figure out what to send for 'config' parameter
    this.get = function(resource) {
        return $http({
            method: 'GET',
            url: AppConfig.baseEndpoint + resource
        });
       // return $http.get(AppConfig.baseEndpoint + resource);
    }
    this.post = function(resource, data) {
        return $http.post(AppConfig.baseEndpoint + resource, data);
    }
});