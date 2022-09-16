function OCTO_Sender() {
    var senderFrom = $("#sender_From").val();
    var senderTo = $("#sender_To").val();
    var flag = 'sender';
    $.get("/dates", { "start_date": senderFrom, "end_date": senderTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function OCTO_Reciever() {
    var recieverFrom = $("#reciever_From").val();
    var recieverTo = $("#reciever_To").val();
    var flag = 'receiver';
    $.get("/dates", { "start_date": recieverFrom, "end_date": recieverTo, "flag": flag });
    setTimeout(function() {window.location.reload();}, 1000)
}


function P2P_Country() {
    var P2PCountryFrom = $("#P2P_Country_From").val();
    var P2PCountryTo = $("#P2P_Country_To").val();
    $.get("/p2p", { "start_date": P2PCountryFrom, "end_date": P2PCountryTo });

}

function P2P_Pinfl() {
    var P2PPinflFrom = $("#P2P_Pinfl_From").val();
    var P2PPinflTo = $("#P2P_Pinfl_To").val();
    $.get("/p2p", { "start_date": P2PPinflFrom, "end_date": P2PPinflTo });
}

function P2P_TT() {
    var P2PTTFrom = $("#P2P_TT_From").val();
    var P2PTTTo = $("#P2P_TT_To").val();
    $.get("/p2p", { "start_date": P2PTTFrom, "end_date": P2PTTTo });
}