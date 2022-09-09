// The HTML table.
var tbl = document.querySelector('.mrotMonth');

// data.
var DsData = [
    { card: 'demo', count: '01748329', amount: '1234', block: 'N', abs: 'Something' },
    { card: 'test', count: '12345789', amount: '4321', block: 'Y', abs: 'Something Else' }
];

// A function to produce a HTML table row as a string.
var template = function template(d) {
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

var render = function render(tbl) {
    return function(d) {
        return tbl.innerHTML += d.map(function(i) {
            return template(i);
        }).join('');
    };
};

// Fire the render function. 
render(tbl)(DsData);