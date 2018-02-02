var chart;

google.load('visualization', '1.1', {'packages':['annotationchart']});
google.setOnLoadCallback(function(){
	chart = new google.visualization.AnnotationChart(document.getElementById('chart_div'));
});


var drawSingleChart = function(seriesId) {
	$.get("data/fred_"+seriesId1+".json", function(s1) {
		var series1  = createDataTable(s1);
		chart.draw(series1, createChartOptions());
	});
}


var drawDoubleChart = function(seriesId1, seriesId2) {

	$.when(
			$.get("data/fred_"+seriesId1+".json"),
			$.get("data/fred_"+seriesId2+".json")
	).then(function(s1, s2) {
		var series1  = createDataTable(s1[0]);
		var series2  = createDataTable(s2[0]);
		var dataTable = google.visualization.data.join(series1, series2, 'full', [[0, 0]], [1], [1]);
		chart.draw(dataTable, createChartOptions());
	});

}


function createDataTable(series){


    var values = series.index.map(function(date, index){
        return [new Date(date), series.data[index][0]];
    });


	// Create the data table
	var dataTable = new google.visualization.DataTable();
	dataTable.addColumn('date', 'Date');
	dataTable.addColumn('number', series.columns[0]);
	dataTable.addRows(values);
	return dataTable;
}

var createChartOptions = function(){
	var fontStyle ='Consolas,Menlo,"Droid Sans Mono","Courier New",monospace';
	var options = {
    		thickness: 2,
    		fill: '50%',
    		displayAnnotations: false,
    		zoomButtons: {
    			  '5-years': { 'label': '5y', 'offset': [5, 0, 0, 0, 0, 0, 0]},
    			  '10-years': { 'label': '10y', 'offset': [10, 0, 0, 0, 0, 0, 0]}
    		},
    		zoomButtonsOrder: ['1-month', '3-months', '6-months', '1-year', ,'5-years','10-years','max'],
    		chart: {
    			interpolateNulls: true,
    			hAxis: {
	    			    textStyle:{
	    			    	color: '#ffffff',
	    			    	fontName: fontStyle,
	    			    },
	    				baselineColor: '#ffff00',
	    			    gridlineColor: '#707074',
    			},
    			vAxis: {
	    			    textStyle:{
	    			    	color: '#ffffff',
	    			    	fontName: fontStyle,
	    			    	fontSize: 10,
	    			    },
	    			    gridlines: {color: '#707074'}
    			},
                backgroundColor: '#393942',
                chartArea: {
                    backgroundColor: '#393942'
                },
                seriesType: 'line',
                curveType: 'none',
                series:{
                    0:{targetAxisIndex:0},
                    1:{targetAxisIndex:1},
                    2:{targetAxisIndex:1}}
            },
            range: {
                ui: {
                    chartOptions: {
                    	interpolateNulls: true,
                    	hAxis: {
            			    textStyle:{
            			    	color: '#ffffff',
            			    	fontName: fontStyle,		
            			    },
            				baselineColor: '#ffff00',
            			    gridlineColor: '#707074',
            			},
            			vAxis: {
            			    textStyle:{color: '#ffffff'},
            			    gridlines: {color: '#707074'}
            			},
                    	
                        backgroundColor: '#393942',
                        chartArea: {
                            'backgroundColor': '#393942'
                        },
                    }
                },
            },
    		colors: ['#FF6544', '#83C449', 'red', 'green', 'yellow', 'gray'],
    };
	return options;
}