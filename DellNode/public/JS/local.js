let code;

let inspiron12;
let xps12;
let alienware12;

$(function() {
    code = $('.region-code').data('region');
    $('a[href$="' + code + '"]').css('color', '#ec407a');

    $('.prediction-form').submit(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/prediction/local',
            type: 'POST',
            data: {
                code: $('#code').val(),
                quater: $('#quater').val()
            },
            success: function(data) {
                drawPrediction(data);
            }
        });
    });

    $.ajax({
        url: '/data/localSales',
        type: 'GET',
        data: { region: code },
        success: function(data) {
            drawSalesChart(data);
        }
    });

    $.ajax({
        url: '/data/localAnalysis',
        type: 'GET',
        data: { region: code },
        success: function(data) {
            drawAdoptionChart(data);
        }
    });

    $.ajax({
        url: '/data/localGeneration',
        type: 'GET',
        data: { region: code },
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

            drawGenerationChart(data);
        }
    });

    $.ajax({
        url: '/data/localOccupations',
        type: 'GET',
        data: { region: code },
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
                        suggestedMax: Math.max(...[Math.max(...data[0]), Math.max(...data[1]), Math.max(...data[2])])+100
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
    data = data.map(function(each_element) {
        return each_element.toFixed(2);
    });

    drawAdoptionData(data);

    var adoptionChart = new Chart(document.querySelector('.adoption-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Alienware', 'Inspiron', 'XPS'],
            datasets: [{
                data: data,
                backgroundColor: ['#D32F2F', '#2196f3', '#263238']
            }]
        }
    });
}

let first = true;
function drawPrediction(data) {
    let inspironbool = data.values[0] >= inspiron12;
    let xpsbool = data.values[1] >= xps12;
    let alienwarebool = data.values[2] >= alienware12;

    let inspironper = (((data.values[0] - inspiron12)/inspiron12) * 100).toFixed(2);
    let xpsper = (((data.values[1] - xps12)/xps12) * 100).toFixed(2);
    let alienwareper = (((data.values[2] - alienware12)/alienware12) * 100).toFixed(2);

    if (!first) {
        $('.predi-text').slideUp("fast", function() {
            $(this).remove();
        });
    } else {
        first = false;
    }

    if (data.recom == 'ext hdd') {
        data.recom = 'External HDD'
    }

    let predictionHTML = `
        <div class="predi-text">
            <ul>
                ${ligen('Inspiron', 400, Math.floor(data.values[0]), inspironper, inspironbool)}
                ${ligen('XPS', 1000, Math.floor(data.values[1]), xpsper, xpsbool)}
                ${ligen('Alienware', 1400, Math.floor(data.values[2]), alienwareper, alienwarebool)}
            </ul>
            <h2 class="padding-left-20">Recommended Accessories: ${data.recom}</h2>
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

function drawAdoptionData(data) {
    let dominatingValue = Math.max(...data);
    let dominatingIndex = -1;

    for (let i = 0; i < data.length; i++) {
        if (parseFloat(dominatingValue) == parseFloat(data[i])) {
            dominatingIndex = i;
            break;
        }
    }

    let dominatingDOM = $('.majority');

    let ad1DOM = $('.ad1');
    let ad2DOM = $('.ad2');
    let ad3DOM = $('.ad3');

    if (dominatingIndex == 0) {
        dominatingDOM.text(`Market Dominance Of Alienware`);
        ad1DOM.text(`Alienware market share ${data[0]}%`);
        if (data[1] >= data[2]) {
            ad2DOM.text(`Inspiron market share ${data[1]}%`);
            ad3DOM.text(`XPS market share ${data[2]}%`);
        } else {
            ad2DOM.text(`XPS market share ${data[2]}%`);
            ad3DOM.text(`Inspiron market share ${data[1]}%`);
        }
    } else if (dominatingIndex == 1) {
        dominatingDOM.text(`Market Dominance Of Inspiron`);
        ad1DOM.text(`Inspiron market share ${data[1]}%`);
        if (data[0] >= data[2]) {
            ad2DOM.text(`Alienware market share ${data[0]}%`);
            ad3DOM.text(`XPS market share ${data[2]}%`);
        } else {
            ad2DOM.text(`XPS market share ${data[2]}%`);
            ad3DOM.text(`Alienware market share ${data[0]}%`);
        }
    } else if (dominatingIndex == 2){
        dominatingDOM.text(`Market Dominance Of XPS`);
        ad1DOM.text(`XPS market share ${data[2]}%`);
        if (data[0] >= data[1]) {
            ad2DOM.text(`Alienware market share ${data[0]}%`);
            ad3DOM.text(`Inspiron market share ${data[1]}%`);
        } else {
            ad2DOM.text(`Inspiron market share ${data[1]}%`);
            ad3DOM.text(`Alienware market share ${data[0]}%`);
        }
    }

}

function drawGenerationChart(data) {
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