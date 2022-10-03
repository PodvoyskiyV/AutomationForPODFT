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
        default_sort_OCTO(1)
    } else if (tabName == "OCTO_Reciever") {
        default_sort_OCTO(2)
    } else if (tabName == "P2P_Country") {
        default_sort_P2P(1);
    } else if (tabName == "P2P_Pinfl") {
        default_sort_P2P(2);
    } else if (tabName == "P2P_TT") {
        default_sort_P2P(3);
    } else if (tabName == "Bank_Offshore") {
        default_sort_Bank(1)
    }
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
    change_flag(sort_tabName)
}


function default_sort_OCTO(flag_sort) {
    if (flag_sort == 1) {
        document.getElementById("Sender_defaultOpen").click();
    } else {
        document.getElementById("Reciever_defaultOpen").click();
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
    }
}

// Change year at footer
var now = new Date().getFullYear();
document.querySelector('span.copyright_Date').innerHTML = now;