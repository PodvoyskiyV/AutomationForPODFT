// The HTML tables.
var mrotMonth = document.querySelector('.mrotMonth');
var mrotWeek = document.querySelector('.mrotWeek');
var mrotDay = document.querySelector('.mrotDay');

function template_mrot_month(d) {
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
            d.abs +
            '</td>' +
            '</tr>';
};

function render_mrot_month(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_mrot_month(i);
            }).join('');
        };
    };

function render_mrot(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_mrot(i);
            }).join('');
        };
    };

function mrot_table_from_back(MonthData, WeekData, DayData) {
    render_mrot_month(mrotMonth)(MonthData);
    render_mrot(mrotWeek)(WeekData);
    render_mrot(mrotDay)(DayData);
    console.log(MonthData)
    console.log(WeekData)
    console.log(DayData)
}

var octoSenderWeek = document.querySelector('.octoSenderWeek');
var octoSenderMonth = document.querySelector('.octoSenderMonth');
var octoSenderFrom = document.querySelector('.octoSenderFrom');
var octoReceiverWeek = document.querySelector('.octoRecieverWeek');
var octoReceiverMonth = document.querySelector('.octoRecieverMonth');
var octoReceiverFrom = document.querySelector('.octoRecieverFrom');

function template_octo_p2p(d) {
        return '<tr>' +
            '<td>' +
            d.id +
            '</td>' +
            '<td>' +
            d.count +
            '</td>' +
            '<td>' +
            d.amount +
            '</td>' +
            '</tr>';
};

function render_octo_p2p(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_octo_p2p(i);
            }).join('');
        };
    };

function octo_table_from_back(sender_week, sender_month, sender_search, receiver_week, receiver_month, receiver_search, tab) {
    render_octo_p2p(octoSenderWeek)(sender_week);
    render_octo_p2p(octoSenderMonth)(sender_month);
    render_octo_p2p(octoSenderFrom)(sender_search);

    render_octo_p2p(octoReceiverWeek)(receiver_week);
    render_octo_p2p(octoReceiverMonth)(receiver_month);
    render_octo_p2p(octoReceiverFrom)(receiver_search);

    if (tab == 'sender') {
        document.getElementById("OCTO_defaultOpen").click();
        document.getElementById("Sender_D_From").click();
    } else if (tab == 'receiver') {
        document.getElementById("OCTO_Tab_Reciever").click();
        document.getElementById("Receiver_D_From").click();
    }
}

var p2pCountryWeek = document.querySelector('.p2pCountryWeek');
var p2pCountryMonth = document.querySelector('.p2pCountryMonth');
var p2pCountryFrom = document.querySelector('.p2pCountryFrom');
var p2pPinflWeek = document.querySelector('.p2pPinflWeek');
var p2pPinflMonth = document.querySelector('.p2pPinflMonth');
var p2pPinflFrom = document.querySelector('.p2pPinflFrom');
var p2pTTWeek = document.querySelector('.p2pTTWeek');
var p2pTTMonth = document.querySelector('.p2pTTMonth');
var p2pTTFrom = document.querySelector('.p2pTTFrom');

function template_p2p(d) {
        return '<tr>' +
            '<td>' +
            d.id +
            '</td>' +
            '<td>' +
            d.count +
            '</td>' +
            '</tr>';
};

function render_p2p(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_p2p(i);
            }).join('');
        };
    };

function p2p_table_from_back(country_week, country_month, country_search, pinfl_week, pinfl_month, pinfl_search, tt_week, tt_month, tt_search, tab) {
    render_octo_p2p(p2pCountryWeek)(country_week);
    console.log(p2pCountryWeek, country_week)
    render_octo_p2p(p2pCountryMonth)(country_month);
    console.log(p2pCountryMonth, country_month)
    render_octo_p2p(p2pCountryFrom)(country_search);

    render_octo_p2p(p2pPinflWeek)(pinfl_week);
    render_octo_p2p(p2pPinflMonth)(pinfl_month);
    render_octo_p2p(p2pPinflFrom)(pinfl_search);

    render_p2p(p2pTTWeek)(tt_week);
    render_p2p(p2pTTMonth)(tt_month);
    render_p2p(p2pTTFrom)(tt_search);

    if (tab == 'country') {
        document.getElementById("P2P_defaultOpen").click();
        document.getElementById("Country_D_From").click();
    } else if (tab == 'pinfl') {
        document.getElementById("P2P_Tab_pinfl").click();
        document.getElementById("Pinfl_D_From").click();
    } else if (tab == 'tt') {
        document.getElementById("P2P_Tab_tt").click();
        document.getElementById("TT_D_From").click();
    }
}

var OffshoreCyprusWeek = document.querySelector('.offshoreCyprusWeek');
var OffshoreCyprusMonth = document.querySelector('.offshoreCyprusMonth');
var OffshoreCyprusFrom = document.querySelector('.offshoreCyprusFrom');

function template_offshore_cyprus(d) {
    return '<tr>' +
            '<td>' +
            d.person +
            '</td>' +
            '<td>' +
            d.birthday +
            '</td>' +
            '<td>' +
            d.passport +
            '</td>' +
            '<td>' +
            d.operation_date +
            '</td>' +
            '<td>' +
            d.amount +
            '</td>' +
            '<td>' +
            d.country +
            '</td>' +
            '</tr>';
};

function render_offshore_cyprus(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_offshore_cyprus(i);
            }).join('');
        };
    };

function offshore_table_from_back(cyprus_week, cyprus_month, cyprus_search, tab) {
    render_offshore_cyprus(OffshoreCyprusWeek)(cyprus_week);
    render_offshore_cyprus(OffshoreCyprusMonth)(cyprus_month);
    render_offshore_cyprus(OffshoreCyprusFrom)(cyprus_search);

    if (tab == 'cyprus') {
        document.getElementById("Cyprus_defaultOpen").click();
        document.getElementById("Cyprus_D_From").click();
    }
}