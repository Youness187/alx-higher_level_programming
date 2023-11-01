$('document').ready(() => {
  $('#btn_translate').click(translate);
  $('#language_code').focus(() => {
    $(this).keydown((e) => {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

const translate = () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $.get(url + $.param({ lang: $('#language_code').val() }),(data) => {
    $('#hello').html(data.hello);
  });
}
