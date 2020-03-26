$(document).ready(function() {
    $("#add-recipe #submit-btn").click(function() {
        var author_name = $("#author_name").val();
        var recipe_name = $("#recipe_name").val();
        var description = $('#description').val();
        var Preparation_time = $('#Preparation_time').val();
        var cooking = $('#cooking').val();
        var ingredients = $('#ingredients').val();
        var methods = $('#methods').val();
        /* Required attr not working on the select tag with materialize.
        The select option tag was hidden and replaced by a unlisted list. So we have to target it.
        - Found this workaround with tutor */
        var select_options = $(".dropdown-content");
        var options_list = $(".dropdown-content li");
        var array_value = true;

        // Check if the fields are not empty
        if (author_name !== '' && recipe_name !== '' && description !== '' && 
            Preparation_time !== '' && cooking !== ''&& ingredients !== '' && methods !== '' && options_list.hasClass("active", "selected")) {
                // For function partially written by a tutor. Had to complete the if statement by myself.
                for(var i; i<select_options.length; i++) {
                    // Check if it has not the class selected. This if function was taken from https://stackoverflow.com/questions/10539162/using-jquery-to-see-if-a-div-has-a-child-with-a-certain-class
                    if (!select_options[i].find('li.selected').length !== 0){
                        array_value = false;
                    }
                }
                if (array_value) {
                    Materialize.toast('You have successfully registered a recipe', 4000)   
                }else {
                    Materialize.toast('Please fill all the required fields', 4000)

                }
        } else {
            Materialize.toast('Please fill all the required fields', 4000)
        }

    });
});