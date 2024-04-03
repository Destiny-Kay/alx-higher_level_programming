$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
    if (textStatus === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
