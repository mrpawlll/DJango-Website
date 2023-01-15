function filterSearch() {
    // Declare variables
    var input, filter, table, tr,td , i, searchValue;
    input = document.getElementById("deliveryorder-search-input");
    filter = input.value()
    table = document.getElementById("deliveryorderTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    // for (i = 0; i < tr.length; i++) {
    // td = tr[i].getElementsByTagName("td")[0];
    //     if (td) {
    //         searchValue = td.textContent || td.innerText;
    //         if (searchValue.indexOf(filter) > -1) {
    //         tr[i].style.display = "";
    //         } else {
    //         tr[i].style.display = "none";
    //         }
    //     }
    // }

    table.style.display = "none";

}

function test(){
    var table,input
    input = document.getElementById("deliveryorder-search-input");
    table = document.getElementById("deliveryorderTable");
    table.style.display = "none";
}