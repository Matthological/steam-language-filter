angular.module("app", []).controller('SteamSearch', function($scope, ServerCommunication){
    ServerCommunication.get('language').then(function(res){
        debugger;
        $scope.languages = res.data;
    }, function(err){
        debugger;
        console.log(err);
    });
});