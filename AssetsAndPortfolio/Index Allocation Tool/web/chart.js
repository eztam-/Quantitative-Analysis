
//var  dat = {"United States":31.155,"China":15.6,"Taiwan":5.765,"Korea (South)":5.76,"India":4.415,"Japan":4.11,"Brazil":4.02,"South Africa":2.815,"United Kingdom":2.705,"Russian Federation":2.045,"France":1.87,"Canada":1.775,"Switzerland":1.61,"Germany":1.545,"Thailand":1.525,"Mexico":1.26,"Australia":1.19,"Malaysia":1.1,"Indonesia":1.095,"Ireland":0.905,"Hong Kong":0.8,"Netherlands":0.605,"Philippines":0.565,"Poland":0.55,"Spain":0.495,"Qatar":0.495,"Chile":0.47,"Sweden":0.435,"United Arab Emirates":0.385,"Italy":0.37,"Denmark":0.3,"Turkey":0.295,"Singapore":0.23,"Colombia":0.23,"Peru":0.195,"Belgium":0.175,"Argentina":0.17,"Finland":0.16,"Greece":0.16,"Hungary":0.15,"European Union":0.125,"Norway":0.12,"Israel":0.1,"Egypt":0.085,"Czech Republic":0.08,"New Zealand":0.04,"Austria":0.04,"Portugal":0.02,"Pakistan":0.015,"Malta":0.0,"-":0.0};


$.getJSON('http://localhost:5000/data.json', function(json) {

    var dat2 = new Array();
    dat2.push(['country', 'Popularity']);
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