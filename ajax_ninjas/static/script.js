$(document).ready(function () {
    $("button").click(function () {
        $(".turtleTitle").remove();
        var turtle = $(this).val();
        $(".col-md-12").prepend(`<h1 class="turtleTitle">${turtle}</h1>`)
        $(".turtleTitle").append(`<img class="turtleImage mx-auto" src="static/img/${turtle}.jpg">`)
    });
});