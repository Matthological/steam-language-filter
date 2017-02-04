angular.module("app", []).controller('SteamSearch', function($scope, ServerCommunication){
    ServerCommunication.get('language').then(function(res){
        $scope.languages = res.data;
    }, function(err){
        console.log(err);
    });
});
