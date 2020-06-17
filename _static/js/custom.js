document.addEventListener('DOMContentLoaded', (event) => {
  alert("Hello! I am an alert box!!");
  p = document.getElementById("rtd-search-form").parentElement;
  p.innerHTML += "Hello";
})


1
// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );
});
