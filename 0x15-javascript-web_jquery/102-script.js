$(function () {
  $('#btn_translate').click(function () {
    const lanCode = $('#language_code');
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lanCode.val();
    $.get(url, function (data, textStatus) {
      if (textStatus === 'success' && data !== null) {
        $('#hello').text(data.hello);
      }
    });
  });
});
