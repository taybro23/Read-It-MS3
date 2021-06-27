$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('input#input_text, textarea#review').characterCounter();
    $('.btn-large').hover(
        function(){
            $(this).removeClass("green", "accent-4")
        },
        function(){
            $(this).addClass("green", "accent-4")
        }
    )
  });