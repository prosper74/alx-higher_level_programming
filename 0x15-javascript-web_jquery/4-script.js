// JavaScript script that toggles the class of the <header>
// element when the user clicks on the tag DIV#toggle_header:
$('DIV#toggle_header').click(function () {
  if ($('HEADER').attr('class') === 'green') {
    $('HEADER').attr('class', 'red');
  } else { $('HEADER').attr('class', 'green'); }
});
