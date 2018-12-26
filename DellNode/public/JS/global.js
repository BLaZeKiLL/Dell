let inspiron12;
let xps12;
let alienware12;

$(function() {
    $('a[href$="/"]').css('color', '#ec407a');
    $('.prediction-form').submit(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/prediction/global',
            type: 'POST',
            data: {
                quater: $('#quater').val()
            },
            success: function(data) {
                drawPrediction(data);
            }
        });
    });

    $.ajax({
        url: '/data/globalAnalysis',
        type: 'GET',
        success: function(data) {
            drawAdoptionChart(data);
        }
    });

    $.ajax({
        url: '/data/globalSales',
        type: 'GET',
        success: function(data) {
            drawSalesChart(data);
        }
    });

    $.ajax({
        url: '/data/globalGenerations',
        type: 'GET',
        success: function(data) {
            data.Inspiron = data.Inspiron.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });
        
            data.XPS = data.XPS.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });
        
            data.AlienWare = data.AlienWare.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });

            drawGenerations(data);
        }
    });

    $.ajax({
        url: '/data/globalOccupations',
        type: 'GET',
        success: function(data) {
            data.Inspiron = data.Inspiron.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });
        
            data.XPS = data.XPS.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });
        
            data.AlienWare = data.AlienWare.map(function(each_element) {
                return parseFloat(each_element.toFixed(2));
            });
            drawOccupations(data);
        }
    });
});

function drawSalesChart(data) {
    data[0] = data[0].map(function(each_element) {
        return Math.floor(each_element);
    });
    inspiron12 = data[0][11];

    data[1] = data[1].map(function(each_element) {
        return Math.floor(each_element);
    });
    xps12 = data[1][11];

    data[2] = data[2].map(function(each_element) {
        return Math.floor(each_element);
    });
    alienware12 = data[2][11];
    
    var saleGraph = new Chart(document.querySelector('.sale-graph').getContext('2d'), {
        type: 'line',
        data: {
            labels: ['1st Quater', '2nd Quater', '3rd Quater', '4th Quater', '5th Quater', '6th Quater', '7th Quater', '8th Quater', '9th Quater', '10th Quater', '11th Quater', '12th Quater'],
            datasets: [{
                label: 'Inspiron',
                borderColor: '#2196f3',
                backgroundColor: '#2196f3',
                fill: false,
                data: data[0]
            }, {
                label: 'XPS',
                borderColor: '#263238',
                backgroundColor: '#263238',
                fill: false,
                data: data[1]
            }, {
                label: 'AlienWare',
                borderColor: '#D32F2F',
                backgroundColor: '#D32F2F',
                fill: false,
                data: data[2]
            }]  
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMax: Math.max(...[Math.max(...data[0]), Math.max(...data[1]), Math.max(...data[2])])+1000
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Sales'
                    }
                }]
            },
            responsive: true
        }
    });
}

function drawAdoptionChart(data) {
    var inspirionChart = new Chart(document.querySelector('.inspiron-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['USC', 'WSE', 'CAJ', 'SEA', 'CA'],
            datasets: [{
                data: [data.Inspiron[3].toFixed(2), data.Inspiron[4].toFixed(2), data.Inspiron[1].toFixed(2), data.Inspiron[2].toFixed(2), data.Inspiron[0].toFixed(2)],
                backgroundColor: ['#90caf9', '#64b5f6', '#2196f3', '#1976d2', '#0d47a1']
            }]
        }
    });
    
    var xpsChart = new Chart(document.querySelector('.xps-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['USC', 'WSE', 'CAJ', 'SEA', 'CA'],
            datasets: [{
                data: [data.XPS[3].toFixed(2), data.XPS[4].toFixed(2), data.XPS[1].toFixed(2), data.XPS[2].toFixed(2), data.XPS[0].toFixed(2)],
                backgroundColor: ['#cfd8dc', '#90a4ae', '#757575', '#546e7a', '#263238']
            }]
        }
    });
    
    var alienwareChart = new Chart(document.querySelector('.alienware-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['USC', 'WSE', 'CAJ', 'SEA', 'CA'],
            datasets: [{
                data: [data.AlienWare[3].toFixed(2), data.AlienWare[4].toFixed(2), data.AlienWare[1].toFixed(2), data.AlienWare[2].toFixed(2), data.AlienWare[0].toFixed(2)],
                backgroundColor: ['#FFCDD2', '#E57373', '#F44336', '#D32F2F', '#B71C1C']
            }]
        }
    });
}

function drawGenerations(data) {
    var generationGraph = new Chart(document.querySelector('.inspiron-generation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Gen 1', 'Gen 2', 'Gen 3'],
            datasets: [{
                data: data.Inspiron,
                backgroundColor: ['#90caf9', '#2196f3', '#0d47a1']
            }]
        }
    });

    var generationGraph = new Chart(document.querySelector('.xps-generation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Gen 1', 'Gen 2', 'Gen 3'],
            datasets: [{
                data: data.XPS,
                backgroundColor: ['#cfd8dc', '#757575', '#263238']
            }]
        }
    });

    var generationGraph = new Chart(document.querySelector('.alienware-generation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Gen 1', 'Gen 2', 'Gen 3'],
            datasets: [{
                data: data.AlienWare,
                backgroundColor: ['#E57373', '#F44336', '#D32F2F']
            }]
        }
    });
}

function drawPrediction(data) {
    $('.predi-text').slideUp("fast", function() {
        $(this).remove();
    })

    let predictionHTML = `
        <h3 class="predi-text">Predicted Sales: ${Math.floor(data.value)} units</h3>
    `;

    $(predictionHTML).appendTo('.predi-card').hide().slideDown("fast");
}

let first = true;
function drawPrediction(data) {
    let inspironbool = data.value[0] >= inspiron12;
    let xpsbool = data.value[1] >= xps12;
    let alienwarebool = data.value[2] >= alienware12;

    let inspironper = (((data.value[0] - inspiron12)/inspiron12) * 100).toFixed(2);
    let xpsper = (((data.value[1] - xps12)/xps12) * 100).toFixed(2);
    let alienwareper = (((data.value[2] - alienware12)/alienware12) * 100).toFixed(2);

    if (!first) {
        $('.predi-text').slideUp("fast", function() {
            $(this).remove();
        });
    } else {
        first = false;
    }

    let predictionHTML = `
        <div class="predi-text">
            <ul>
                ${ligen('Inspiron', 400, Math.floor(data.value[0]), inspironper, inspironbool)}
                ${ligen('XPS', 1000, Math.floor(data.value[1]), xpsper, xpsbool)}
                ${ligen('Alienware', 1400, Math.floor(data.value[2]), alienwareper, alienwarebool)}
            </ul>
        </div>
    `;

    $(predictionHTML).appendTo('.predi-card').hide().slideDown("fast");
}

function ligen(model, cost, val, per, bool) {
    let liHTML = `<li><h3>${model}: $${val * cost} `;

    if (bool) {
        liHTML += ` (${per}%<span style="color:green"><i class="glyphicon glyphicon-triangle-top"></i></span>)</h3></li>`
    } else {
        liHTML += ` (${per}%<span style="color:red"><i class="glyphicon glyphicon-triangle-bottom"></i></span>)</h3></li>`
    }

    return liHTML;
}

function drawOccupations(data) {
    var generationGraph = new Chart(document.querySelector('.inspiron-occupation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Businessman', 'Developer', 'Farmer', 'Gamer', 'Manager', 'Student'],
            datasets: [{
                data: data.Inspiron,
                backgroundColor: ['#90caf9', '#64b5f6', '#2196f3', '#1976d2', '#0d47a1', '#021350']
            }]
        }
    });

    var generationGraph = new Chart(document.querySelector('.xps-occupation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Businessman', 'Developer', 'Farmer', 'Gamer', 'Manager', 'Student'],
            datasets: [{
                data: data.XPS,
                backgroundColor: ['#cfd8dc', '#90a4ae', '#757575', '#546e7a', '#263238', '#0a0a0a']
            }]
        }
    });

    var generationGraph = new Chart(document.querySelector('.alienware-occupation-graph').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Businessman', 'Developer', 'Farmer', 'Gamer', 'Manager', 'Student'],
            datasets: [{
                data: data.AlienWare,
                backgroundColor: ['#FFCDD2', '#E57373', '#F44336', '#D32F2F', '#B71C1C', '#610b05']
            }]
        }
    });
}