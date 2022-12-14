function OCTO_Sender() {
    var senderFrom = $("#sender_From").val();
    var senderTo = $("#sender_To").val();
    var flag = 'sender';
    $.get("/dates", { "start_date": senderFrom, "end_date": senderTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function OCTO_Receiver() {
    var receiverFrom = $("#receiver_From").val();
    var receiverTo = $("#receiver_To").val();
    var flag = 'receiver';
    $.get("/dates", { "start_date": receiverFrom, "end_date": receiverTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function P2P_Country() {
    var P2PCountryFrom = $("#P2P_Country_From").val();
    var P2PCountryTo = $("#P2P_Country_To").val();
    var flag = 'country';
    $.get("/dates", { "start_date": P2PCountryFrom, "end_date": P2PCountryTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function P2P_Pinfl() {
    var P2PPinflFrom = $("#P2P_Pinfl_From").val();
    var P2PPinflTo = $("#P2P_Pinfl_To").val();
    var flag = 'pinfl';
    $.get("/dates", { "start_date": P2PPinflFrom, "end_date": P2PPinflTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function P2P_TT() {
    var P2PTTFrom = $("#p2p_tt_from").val();
    var P2PTTTo = $("#p2p_tt_to").val();
    var flag = 'tt';
    $.get("/dates", { "start_date": P2PTTFrom, "end_date": P2PTTTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Bank_Offshore() {
    var BankOffshoreFrom = $("#bank_Offshore_From").val();
    var BankOffshoreTo = $("#bank_Offshore_To").val();
    var flag = 'offshore';
    $.get("/dates", { "start_date": BankOffshoreFrom, "end_date": BankOffshoreTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Bank_Questions() {
    var BankQuestionsFrom = $("#bank_Questions_From").val();
    var BankQuestionsTo = $("#bank_Questions_To").val();
    var flag = 'questions';
    $.get("/dates", { "start_date": BankQuestionsFrom, "end_date": BankQuestionsTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Bank_BRV() {
    var BankBRVFrom = $("#bank_BRV_From").val();
    var BankBRVTo = $("#bank_BRV_To").val();
    var flag = 'brv';
    $.get("/dates", { "start_date": BankBRVFrom, "end_date": BankBRVTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Bank_FATF() {
    var BankFATFFrom = $("#bank_FATF_From").val();
    var BankFATFTo = $("#bank_FATF_To").val();
    var flag = 'fatf';
    $.get("/dates", { "start_date": BankFATFFrom, "end_date": BankFATFTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Bank_Terrorism() {
    var BankTerrorismFrom = $("#bank_Terrorism_From").val();
    var BankTerrorismTo = $("#bank_Terrorism_To").val();
    var flag = 'terrorism';
    $.get("/dates", { "start_date": BankTerrorismFrom, "end_date": BankTerrorismTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}
