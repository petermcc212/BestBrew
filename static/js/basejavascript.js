// Menu toggle script on base
    $(document).ready(function() {
        $("#menu-toggle").click( function(e) {
            e.preventDefault();
            $("#wrapper").toggleClass("menuDisplayed");
    
        });
        });


// Autocomplete search field on base
    $(document).ready(function(){
        $("#suggestion").autocomplete({
            source: "/rango/autocomplete/",
            minLength: 1,
            });
    });
