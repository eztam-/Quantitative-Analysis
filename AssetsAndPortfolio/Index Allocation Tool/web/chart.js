
$.getJSON('/data.json', function(json) {

    var dat2 = new Array();
    dat2.push(['Country', 'Exposure (%)']);
    for (var key in json.country) {
        dat2.push([key, json.country[key]]);
    }

    google.charts.load('current', {
            'packages':['geochart'],
            // Note: you will need to get a mapsApiKey for your project.
            // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
            'mapsApiKey': 'AIzaSyBzHZjpzSiusaSN8Xgm_Q4pfRopXWiWRWs'
          });
          google.charts.setOnLoadCallback(drawRegionsMap);

          function drawRegionsMap() {
            var data = google.visualization.arrayToDataTable(dat2);

            var options = {};

            var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

            chart.draw(data, options);
          }



            fillTable('#country-table', 'Country', 'Weight (%)', json.country);
            fillTable('#instrument-table', 'Stock', 'Weight (%)', json.instrument);
            fillTable('#ccy-table', 'Currency', 'Weight (%)', json.ccy);
            fillTable('#sector-table', 'Sector', 'Weight (%)', json.sector);



});



function fillTable(tabId, title1, title2, data){
    var tableData = new Array();
    for (var key in data) {
        tableData.push([key, data[key]]);
    }
    $(tabId).DataTable({
      data: tableData,
      order: [[ 1, "desc" ]],
      columns: [
              { title: title1 },
              { title: title2 } ]
    });

}