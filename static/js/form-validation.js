$(document).ready(function() {
    $("#submit-btn").click(function() {
        var author_name = $("#author_name").val();
        var recipe_name = $("#recipe_name").val();
        var description = $('#description').val();
        var Preparation_time = $('#Preparation_time').val();
        var cooking = $('#cooking').val();
        var ingredients = $('#ingredients').val();
        var methods = $('#methods').val();
        /* This replace the select options elements because 
        they are actually hidden from view, and replaced with something else. */
        var select_options = $(".select-dropdown li");

        // Check if the fields are not empty
        if (author_name !== '' && recipe_name !== ''&& description !== ''&& 
            Preparation_time !== ''&& cooking !== ''&& ingredients !== ''&& methods !== '' && select_option.hasClass("active", "selected")) {
                Materialize.toast('You have successfully registered a recipe', 4000)
        } else {
            Materialize.toast('Please fill all the required fields', 4000)
        }

    });
});