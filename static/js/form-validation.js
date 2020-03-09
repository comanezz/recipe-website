$(document).ready(function() {
    $("#submit-btn").click(function() {
        var author_name = $("#author_name").val();
        var servings = $("#servings").val();
        var recipe_name = $("#recipe_name").val();
        var description = $('#description').val();
        var recipe_type = $('#recipe_type').val();
        var Preparation_time = $('#Preparation_time').val();
        var cooking = $('#cooking').val();
        var ingredients = $('#ingredients').val();
        var methods = $('#methods').val();

        // Check if the fiels are empty or not
        if (author_name == '' || servings == '' || recipe_name == ''|| description == ''|| 
            recipe_type == ''|| Preparation_time == ''|| cooking == ''|| ingredients == ''|| methods == '') {
            alert("Please fill all the fields !")
            return false;
        } else {
            alert('You have successfully registered a recipe')
        }
    });
});