// The HTML tables.
var mrotMonth = document.querySelector('.mrotMonth');
var mrotDynamics = document.querySelector('.mrotDynamics');

var octoSenderWeek = document.querySelector('.octoSenderWeek');
var octoSenderMonth = document.querySelector('.octoSenderMonth');
var octoSenderFrom = document.querySelector('.octoSenderFrom');
var octoReceiverWeek = document.querySelector('.octoRecieverWeek');
var octoReceiverMonth = document.querySelector('.octoRecieverMonth');
var octoReceiverFrom = document.querySelector('.octoRecieverFrom');


function template_mrot(d) {
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

function render_mrot(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_mrot(i);
            }).join('');
        };
    };

function mrot_table_from_back(MonthData, DynamicsData) {
    render_mrot(mrotMonth)(MonthData);
    render_mrot(mrotDynamics)(DynamicsData);
}


function template_octo(d) {
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
            '</tr>';
};

function render_octo(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_octo(i);
            }).join('');
        };
    };

function octo_table_from_back(sender_week, sender_month, sender_from, receiver_week, receiver_month, receiver_search, tab) {
    render_octo(octoSenderWeek)(sender_week);
    render_octo(octoSenderMonth)(sender_month);
    render_octo(octoSenderFrom)(sender_from);

    render_octo(octoReceiverWeek)(receiver_week);
    render_octo(octoReceiverMonth)(receiver_month);
    render_octo(octoReceiverFrom)(receiver_search);

    if (tab == 'sender') {
        document.getElementById("OCTO_defaultOpen").click();
        document.getElementById("Sender_D_From").click();
    } else if (tab == 'receiver') {
        document.getElementById("OCTO_Tab_Reciever").click();
        document.getElementById("Receiver_D_From").click();
    }

}


