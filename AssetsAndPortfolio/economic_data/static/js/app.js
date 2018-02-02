var app = angular.module('erApp', []);
 



app.controller('indicatorCtrl', ['$scope','$http', function ($scope, $http) {
 	
	 $http.get('data/indicators').
     success(function(data) {
    	 $scope.series = data;
    	 $scope.mainSeries = "DTWEXO"
    	 $scope.compareSeries = "FEDFUNDS";
    	 $scope.updateChart();
     });
	 

	$scope.updateChart = function(){
		if($scope.compareSeries){
			drawDoubleChart($scope.mainSeries, $scope.compareSeries);
		}else{
			drawSingleChart($scope.mainSeries);
		}
	}

 	
}]);


app.controller('toolsCtrl', ['$scope', function ($scope) {
 	
		$scope.grahamNumber = {
				eps: 0,
				bps: 0,
				result: 0
				};
		
		$scope.calcGrahamNum = function(){
			$scope.grahamNumber.result = Math.sqrt(22.5*$scope.grahamNumber.eps * $scope.grahamNumber.bps);
		}
			
}]);

