// The HTML tables.

// <----------------------------- MROT ----------------------------->

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

// <----------------------------- OCTO ----------------------------->

var octoSenderWeek = document.querySelector('.octoSenderWeek');
var octoSenderMonth = document.querySelector('.octoSenderMonth');
var octoSenderFrom = document.querySelector('.octoSenderFrom');
var octoReceiverWeek = document.querySelector('.octoReceiverWeek');
var octoReceiverMonth = document.querySelector('.octoReceiverMonth');
var octoReceiverFrom = document.querySelector('.octoReceiverFrom');

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
        document.getElementById("OCTO_Tab_Receiver").click();
        document.getElementById("Receiver_D_From").click();
    }
}

// <----------------------------- P2P ----------------------------->

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
    render_octo_p2p(p2pCountryMonth)(country_month);
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

// <----------------------------- BANK ----------------------------->

var BankOffshoreDay = document.querySelector('.bankOffshoreDay');
var BankOffshoreFrom = document.querySelector('.bankOffshoreFrom');
var BankQuestionsDay = document.querySelector('.bankQuestionsDay');
var BankQuestionsFrom = document.querySelector('.bankQuestionsFrom');
var BankBRVMonth = document.querySelector('.bankBRVMonth');
var BankBRVDay = document.querySelector('.bankBRVDay');

function template_bank_offshore(d) {
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

function render_bank_offshore(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_bank_offshore(i);
            }).join('');
        };
    };

function template_bank_questions(d) {
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
            d.merchant +
            '</td>' +
            '<td>' +
            d.mcc +
            '</td>' +
            '</tr>';
};

function render_bank_questions(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_bank_questions(i);
            }).join('');
        };
    };

function template_bank_brv(d) {
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
            d.amount +
            '</td>' +
            '<td>' +
            d.block +
            '</td>' +
            '<td>' +
            d.observation +
            '</td>' +
            '</tr>';
};

function render_bank_brv(table) {
        return function(d) {
            return table.innerHTML += d.map(function(i) {
                return template_bank_brv(i);
            }).join('');
        };
    };

function bank_table_from_back(offshore_day, offshore_search, questions_day, questions_from, brv_month, brv_day, tab) {
    render_bank_offshore(BankOffshoreDay)(offshore_day);
    render_bank_offshore(BankOffshoreFrom)(offshore_search);
    render_bank_questions(BankQuestionsDay)(questions_day);
    render_bank_questions(BankQuestionsFrom)(questions_from);
    render_bank_brv(BankBRVMonth)(brv_month);
    render_bank_brv(BankBRVDay)(brv_day);

    if (tab == 'offshore') {
        document.getElementById("Bank_defaultOpen").click();
        document.getElementById("Offshore_D_From").click();
    } else if (tab == 'questions') {
        document.getElementById("Bank_Tab_Questions").click();
        document.getElementById("Questions_D_From").click();
    }
}