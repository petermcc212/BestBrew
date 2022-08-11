<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script type="text/javascript" src="/resources/events.js"></script>

<script>
$('#js-tag').html(Urls.base());
$("#menu-toggle").click( function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("menuDisplayed");

});
</script>