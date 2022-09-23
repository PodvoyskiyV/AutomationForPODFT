function OCTO_Sender() {
    var senderFrom = $("#sender_From").val();
    var senderTo = $("#sender_To").val();
    var flag = 'sender';
    $.get("/dates_octo", { "start_date": senderFrom, "end_date": senderTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function OCTO_Reciever() {
    var recieverFrom = $("#reciever_From").val();
    var recieverTo = $("#reciever_To").val();
    var flag = 'receiver';
    $.get("/dates_octo", { "start_date": recieverFrom, "end_date": recieverTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function P2P_Country() {
    var P2PCountryFrom = $("#P2P_Country_From").val();
    var P2PCountryTo = $("#P2P_Country_To").val();
    var flag = 'country';
    $.get("/dates_p2p", { "start_date": P2PCountryFrom, "end_date": P2PCountryTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function P2P_Pinfl() {
    var P2PPinflFrom = $("#P2P_Pinfl_From").val();
    var P2PPinflTo = $("#P2P_Pinfl_To").val();
    var flag = 'pinfl';
    $.get("/dates_p2p", { "start_date": P2PPinflFrom, "end_date": P2PPinflTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function P2P_TT() {
    var P2PTTFrom = $("#p2p_tt_from").val();
    var P2PTTTo = $("#p2p_tt_to").val();
    var flag = 'tt';
    $.get("/dates_p2p", { "start_date": P2PTTFrom, "end_date": P2PTTTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}

function Offshore_Cyprus() {
    var OffshoreCyprusFrom = $("#offshore_Cyprus_From").val();
    var OffshoreCyprusTo = $("#offshore_Cyprus_To").val();
    var flag = 'cyprus';
    $.get("/dates_offshore", { "start_date": OffshoreCyprusFrom, "end_date": OffshoreCyprusTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}