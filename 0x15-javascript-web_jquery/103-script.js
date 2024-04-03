$(function () {
  function sayHello () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val(), function (data, textStatus) {
      if (textStatus === 'success' && data !== null) {
        $('#hello').text(data.hello);
      }
    });
  }
  $('#btn_translate').click(sayHello);
  $('#btn_translate').keypress(function (event) {
    if (event.keyCode === 13) {
      sayHello();
    }
  });
});
