(function() {

    var app = angular.module('PMAPP',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/home', {
            templateUrl: 'pages/home.html',
           controller: 'HomeController',
           controllerAs : 'homeCtrl'
        }).when('/users', {
            templateUrl: 'pages/users.html',
           controller: 'UsersController',
           controllerAs : 'usersCtrl'
        }).when('/groups', {
            templateUrl: 'pages/groups.html',
           controller: 'GroupsController',
           controllerAs : 'groupsCtrl'
        }).when('/groupMembers', {
            templateUrl: 'pages/groupMembers.html',
           controller: 'GroupMembersController',
           controllerAs : 'gMembersCtrl'
        }).when('/contacts', {
            templateUrl: 'pages/contacts.html',
           controller: 'ContactsController',
           controllerAs : 'contactsCtrl'
        }).when('/messagesByGroup/:gid', {
            templateUrl: 'pages/messagesByGroup.html',
           controller: 'MessagesByGroupController',
           controllerAs : 'mbgCtrl'
        }).when('/likes', {
            templateUrl: 'pages/likes.html',
           controller: 'LikesController',
           controllerAs : 'likesCtrl'
        }).when('/dislikes', {
            templateUrl: 'pages/dislikes.html',
           controller: 'DislikesController',
           controllerAs : 'dislikesCtrl'
        }).when('/userInfo/:uid', {
            templateUrl: 'pages/userInfo.html',
            controller: 'UserInfoController',
            controllerAs : 'userInfoCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);

})();

