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

    // if (tabName == 'Reciever') {
    //     document.getElementById("Reciever_sort_defaultOpen").click();
    // } else {
    //     document.getElementById("sort_defaultOpen").click();
    // }

    document.getElementById(`${tabName}_defaultOpen`).click();
}

document.getElementById("defaultOpen").click();

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