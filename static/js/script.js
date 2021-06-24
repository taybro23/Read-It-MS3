$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.btn-large').hover(
        function(){
            $(this).removeClass("green", "accent-4")
        },
        function(){
            $(this).addClass("green", "accent-4")
        }
    )
  });