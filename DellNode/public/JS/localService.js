let code

$(function() {
    code = $('.region-code').data('region');
    $('a[href$="' + code + 'Service"]').css('color', '#ec407a');
    $.ajax({
        url: '/service/local',
        type: 'GET',
        data: { code: code },
        success: function(data) {
            drawCharts(data);
        }
    });
});

function drawCharts(data) {
    new Chart(document.querySelector('.region-chart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['charger fails', 'display fails', 'keyboard fails', 'laptop slow', 'laptop overheats'],
            datasets: [{
                data: data.main,
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#AB5697', '#DF5A1C']
            }]
        },
        options: {
            legend: {
               display: false
            },
        }
    });

    new Chart(document.querySelector('.charger-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['voltage fluctuations', 'battery swelling', 'earthing', 'others'],
            datasets: [{
                data: data.prob['charger fails'],
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#BB4678']
            }]
        }
    });

    new Chart(document.querySelector('.display-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['cracked display', 'gpu failure', 'bios failure', 'others'],
            datasets: [{
                data: data.prob['display fails'],
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#BB4678']
            }]
        }
    });

    new Chart(document.querySelector('.keyboard-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['broken keys', 'liquid damage', 'short circuit', 'others'],
            datasets: [{
                data: data.prob['keyboard fails'],
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#BB4678']
            }]
        }
    });

    new Chart(document.querySelector('.slow-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['ram overusage', 'outdated os', 'harddisk fragmentation', 'others'],
            datasets: [{
                data: data.prob['laptop slow'],
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#BB4678']
            }]
        }
    });

    new Chart(document.querySelector('.overheat-chart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['fan failure', 'heatsink failure', 'high environment temperature', 'others'],
            datasets: [{
                data: data.prob['laptop overheats'],
                backgroundColor: ['#cfd8dc', '#757575', '#263238', '#BB4678']
            }]
        }
    });
}