// open menu
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".close-menu");

sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    sidebarBtn.classList.toggle("open-menu");
});

// Open tab sidebar
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active-tablinks", "");
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
    } else if (tabName == "Offshore_Cyprus") {
        default_sort_Offshore(1)
    }
}

if (document.getElementById("Mrot_defaultOpen")) {
    document.getElementById("Mrot_defaultOpen").click();
} else if (document.getElementById("OCTO_defaultOpen")) {
    document.getElementById("OCTO_defaultOpen").click();
} else if (document.getElementById("P2P_defaultOpen")) {
    document.getElementById("P2P_defaultOpen").click();
} else if (document.getElementById("Offshore_defaultOpen")) {
    document.getElementById("Offshore_defaultOpen").click();
}

// Open table_sort tab
function openSort(evt, sort_tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("sort_tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("sort_tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" sort_active", "");
    }

    document.getElementById(sort_tabName).style.display = "block";
    evt.currentTarget.className += " sort_active";
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

function default_sort_Offshore(flag_sort) {
    if (flag_sort == 1) {
        document.getElementById("Cyprus_defaultOpen").click();
    }
}

// Изменение года в футере
var now = new Date().getFullYear();
document.querySelector('span.copyright_Date').innerHTML = now;