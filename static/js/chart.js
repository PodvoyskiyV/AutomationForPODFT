// Chart 1 ------------------------------------------------------
var chartFirstValues = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000];
new Chart("chartFirst", {
    type: "line",
    data: {
        labels: chartFirstValues,
        datasets: [{
            data: [860, 1140, 1060, 1060, 1070, 1110, 1330, 2210, 7830, 2478],
            borderColor: "#85F4FA",
            fill: false,
            label: "first",
            backgroundColor: "#85F4FA"
        }, {
            data: [1600, 1700, 1700, 1900, 2000, 2700, 4000, 5000, 6000, 7000],
            borderColor: "#3A57E8",
            fill: false,
            label: "second",
            color: "#fff",
            backgroundColor: "#3A57E8"
        }, {
            data: [300, 700, 2000, 5000, 6000, 4000, 2000, 1000, 200, 100],
            borderColor: "#5C6CA5",
            fill: false,
            label: "third",
            backgroundColor: "#5C6CA5"
        }]
    },
    options: {
        legend: { display: true }
    }
});


// Chart 2 ------------------------------------------------------

var chartSecondValuesX = ["1", "2", "3", "4", "5"];
var chartSecondValuesY = [55, 49, 44, 24, 15];
var barColors = ["#85F4FA", "#8A92A6", "#AAAD5F", "#6CA161", "#3A57E8"];

new Chart("chartSecond", {
    type: "bar",
    data: {
        labels: chartSecondValuesX,
        datasets: [{
            backgroundColor: barColors,
            data: chartSecondValuesY
        }]
    },
    options: {
        legend: { display: false },
        title: {
            display: true,
            text: "World Production 2022"
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        }

    }
});

// Chart 3 ------------------------------------------------------

new Chart("chartThird", {
    type: 'bubble',
    data: {
        labels: "Africa",
        datasets: [{
            label: ["China"],
            backgroundColor: "rgba(255,221,50,0.2)",
            borderColor: "rgba(255,221,50,1)",
            data: [{
                x: 21269017,
                y: 5.245,
                r: 15
            }]
        }, {
            label: ["Denmark"],
            backgroundColor: "rgba(60,186,159,0.2)",
            borderColor: "rgba(60,186,159,1)",
            data: [{
                x: 258702,
                y: 7.526,
                r: 10
            }]
        }, {
            label: ["Germany"],
            backgroundColor: "rgba(0,0,0,0.2)",
            borderColor: "#000",
            data: [{
                x: 3979083,
                y: 6.994,
                r: 28
            }]
        }, {
            label: ["Japan"],
            backgroundColor: "rgba(193,46,12,0.2)",
            borderColor: "rgba(193,46,12,1)",
            data: [{
                x: 4931877,
                y: 5.921,
                r: 50
            }]
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Trafic'
        },
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: "Company"
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: "Mobile"
                }
            }]
        }
    }
});