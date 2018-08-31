var chartInterval = null;

$("#logo").click(function(){


var htmltext = "<h3>Welcome To AWS Metrics Dashboard</h3>"+
  "<p>Click on the menu to see the statistics.</p>";
$("#container").html(htmltext);	
	
});

$(".show-metrics").click(function(){
	
	
	var linkText = $(this).text();
	var assignYAxis = null;
	if(linkText==='AllInstanceCPUUsage'||linkText==='AllInstanceDBUsage'){
		
		assignYAxis = yAxis2;
		
	}else{
	
		assignYAxis = yAxis1;
	}
	
	displayChart(linkText,assignYAxis);
	clearInterval(chartInterval);
	chartInterval = setInterval(function(){
		
	$.get("http://52.15.80.38/index.php?display="+linkText, function(data, status){
        displayChart(linkText,assignYAxis);
    });	
		
	},10000);
	
});


yAxis1 = {
        max: 1000,
        title: true,
        plotBands: [{
            from: 0,
            to: 30,
            color: '#E8F5E9'
        }, {
            from: 30,
            to: 70,
            color: '#FFFDE7'
        }, {
            from: 70,
            to: 100,
            color: "#FFEBEE"
        },
		{
            from: 100,
            to: 20000,
            color: '#E8F5E9'
        },{
            from: 100,
            to: 10000,
            color: '#E8F5E9'
        }]
    };
	
yAxis2 = {
        max: 10,
        title: true,
        plotBands: [{
            from: 0.1,
            to: 1,
            color: '#E8F5E9'
        }, {
            from: 1,
            to: 1.5,
            color: '#FFFDE7'
        }, {
            from: 1.5,
            to: 2,
            color: "#FFEBEE"
        },
		{
            from: 2,
            to: 2.5,
            color: '#E8F5E9'
        },{
            from: 2.5,
            to: 3,
            color: '#FFFDE7'
        },{
            from: 3,
            to: 3.5,
            color: "#FFEBEE"
        }, {
            from: 3.5,
            to: 4,
            color: '#FFFDE7'
        }, {
            from: 4,
            to: 5,
            color: '#E8F5E9'
        },{
            from: 5,
            to: 10,
            color: "#FFEBEE"
        }]
    };
function displayChart(linkText,assignYAxis){
var chartObj = {
    chart: {
        type: 'bar',
        height: 800
    },
    title: {
        text: 'AWS Cloud Metrics Dashboard'
    },
    legend: {
        enabled: false
    },
    subtitle: {
        text: linkText
    },
    data: {
		cache:false,
        csvURL: 'http://52.15.80.38/output/'+linkText+'.csv',
        enablePolling: true,
        dataRefreshRate: 1
    },
    plotOptions: {
        bar: {
            colorByPoint: true
        },
        series: {
            zones: [{
                color: '#4CAF50',
                value: 0
            }, {
                color: '#8BC34A',
                value: 10
            }, {
                color: '#CDDC39',
                value: 20
            }, {
                color: '#CDDC39',
                value: 30
            }, {
                color: '#FFEB3B',
                value: 40
            }, {
                color: '#FFEB3B',
                value: 50
            }, {
                color: '#FFC107',
                value: 60
            }, {
                color: '#FF9800',
                value: 70
            }, {
                color: '#FF5722',
                value: 80
            }, {
                color: '#F44336',
                value: 90
            }, {
                color: '#F44336',
                value: Number.MAX_VALUE
            }],
            dataLabels: {
                enabled: true,
                format: '{point.y:.0f}'
            }
        }
    },
    tooltip: {
        valueDecimals: 1,
        valueSuffix: ''
    },
    xAxis: {
		type: 'category',
        labels: {
            style: {
                fontSize: '10px'
            }
        }
    },
    yAxis: assignYAxis
};

Highcharts.chart('container', chartObj);

}