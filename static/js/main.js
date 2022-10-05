// Open menu
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".close-menu");

sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    sidebarBtn.classList.toggle("open-menu");
});

// Open tab sidebar
function openTab(evt, tabName) {
    var i, tab_content, tab_links;
    tab_content = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tab_content.length; i++) {
        tab_content[i].style.display = "none";
    }
    tab_links = document.getElementsByClassName("tablinks");
    for (i = 0; i < tab_links.length; i++) {
        tab_links[i].className = tab_links[i].className.replace(" active-tablinks", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active-tablinks";

    if (tabName == "OCTO_Sender") {
        default_sort_OCTO(1);
    } else if (tabName == "OCTO_Receiver") {
        default_sort_OCTO(2);
    } else if (tabName == "P2P_Country") {
        default_sort_P2P(1);
    } else if (tabName == "P2P_Pinfl") {
        default_sort_P2P(2);
    } else if (tabName == "P2P_TT") {
        default_sort_P2P(3);
    } else if (tabName == "Bank_Offshore") {
        default_sort_Bank(1);
    } else if (tabName == "Bank_Questions") {
        default_sort_Bank(2);
    } else if (tabName == "Bank_BRV") {
        default_sort_Bank(3);
    } else if (tabName == "Bank_FATF") {
        default_sort_Bank(4);
    } else if (tabName == "Bank_Terrorism") {
        default_sort_Bank(5);
    }

    var flag = tabName;
    $.get("/download_tab", { "flag": flag });
}

if (document.getElementById("Mrot_defaultOpen")) {
    document.getElementById("Mrot_defaultOpen").click();
} else if (document.getElementById("OCTO_defaultOpen")) {
    document.getElementById("OCTO_defaultOpen").click();
} else if (document.getElementById("P2P_defaultOpen")) {
    document.getElementById("P2P_defaultOpen").click();
} else if (document.getElementById("Bank_defaultOpen")) {
    document.getElementById("Bank_defaultOpen").click();
}

// Open table_sort tab
function openSort(evt, sort_tabName) {
    var i, tab_content, tab_links;
    tab_content = document.getElementsByClassName("sort_tabcontent");
    for (i = 0; i < tab_content.length; i++) {
        tab_content[i].style.display = "none";
    }

    tab_links = document.getElementsByClassName("sort_tablinks");
    for (i = 0; i < tab_links.length; i++) {
        tab_links[i].className = tab_links[i].className.replace(" sort_active", "");
    }

    document.getElementById(sort_tabName).style.display = "block";
    evt.currentTarget.className += " sort_active";

    var flag = sort_tabName;
    $.get("/download_sort", { "flag": flag });
}


function default_sort_OCTO(flag_sort) {
    if (flag_sort == 1) {
        document.getElementById("Sender_defaultOpen").click();
    } else if (flag_sort == 2) {
        document.getElementById("Receiver_defaultOpen").click();
    }
}

function default_sort_P2P(flag_sort) {
    if (flag_sort == 1) {
        document.getElementById("Country_defaultOpen").click();
    } else if (flag_sort == 2) {
        document.getElementById("Pinfl_defaultOpen").click();
    } else if (flag_sort == 3) {
        document.getElementById("P2P_TT_defaultOpen").click();
    }
}

function default_sort_Bank(flag_sort) {
    if (flag_sort == 1) {
        document.getElementById("Offshore_defaultOpen").click();
    } else if (flag_sort == 2) {
        document.getElementById("Questions_defaultOpen").click();
    } else if (flag_sort == 3) {
        document.getElementById("BRV_defaultOpen").click();
    } else if (flag_sort == 4) {
        document.getElementById("FATF_defaultOpen").click();
    } else if (flag_sort == 5) {
        document.getElementById("Terrorism_defaultOpen").click();
    }
}

// Change year at footer
var now = new Date().getFullYear();
document.querySelector('span.copyright_Date').innerHTML = now;