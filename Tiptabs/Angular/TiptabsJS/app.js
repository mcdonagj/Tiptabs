'use strict'

var app = angular.module('tiptabs_app', ['ngMaterial', 'ngMessages']);

    app.config(['$interpolateProvider', function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
    }]);

    app.controller("app_controller", function ($scope, $http, $mdDialog) {
        $scope.available_rates = JSON.parse('{{rates | tojson}}');
        $scope.response = {};
        $scope.status = '  ';
        $scope.resetForm = function (ev) {
            var confirm = $mdDialog.confirm()
                .title('Are you sure?')
                .textContent('All entered information will be lost!')
                .targetEvent(ev)
                .ok('Reset Form.')
                .cancel('Cancel');

            $mdDialog.show(confirm).then(function () {
                $scope.status = 'Form Reset.';
            }, function () {
                $scope.status = 'Decided to cancel.';
            });
        };
        
        $scope.showConfirm = function (ev) {
            var confirm = $mdDialog.confirm()
                .title('Calculate a Tip Amount?')
                .textContent('You\'ve chosen to convert {{BILL_AMOUNT}} in {{BASE_CURRENCY}} to {{CONVERTED_CURRENCY}}.' +
                    '\n{{TIP_PERCENTAGE}} of {{BASE_CURRENCY}} will be added to your total in {{CONVERTED_CURRENCY}}.')
                .targetEvent(ev)
                .ok('Calculate Tip')
                .cancel('Cancel');

            $mdDialog.show(confirm).then(function () {
                document.getElementById("Input-Form").submit();
                $scope.status = 'Your converted total is..';
            }, function () {
                $scope.status = 'Decided to cancel.';
            });
        };
        $scope.sendResponse = function () {
            $http.post('/', $scope.response, { 'Content-Type': 'application/x-www-form-urlencoded' })
        };
    })