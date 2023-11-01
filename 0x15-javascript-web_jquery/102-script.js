$('document').ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('#btn_translate').click(() => {
    $.get(url + $.param({ lang: $('#language_code').val() }), (data) => {
      $('#hello').html(data.hello);
    });
  });
});
