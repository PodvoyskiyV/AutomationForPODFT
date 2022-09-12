// The HTML table.
var mrotMonth = document.querySelector('.mrotMonth');
var mrotDynamics = document.querySelector('.mrotDynamics');

function template(d) {
        return '<tr>' +
            '<td>' +
            d.card +
            '</td>' +
            '<td>' +
            d.count +
            '</td>' +
            '<td>' +
            d.amount +
            '</td>' +
            '<td>' +
            d.block +
            '</td>' +
            '<td>' +
            d.abs +
            '</td>' +
            '</tr>';
    };

function render(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template(i);
            }).join('');
        };
    };

function mrot_table_from_back(MonthData, DynamicsData) {
    console.log(MonthData)
    console.log(DynamicsData)

    render(mrotMonth)(MonthData);
    render(mrotDynamics)(DynamicsData);
}

