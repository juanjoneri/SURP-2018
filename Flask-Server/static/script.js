$(document).ready(function(){
  console.log('ready')

  $('#reaction').click(() => {
    $('#reaction-files').click();
  });

  $('#cards').click(() => {
    $('#card-files').click();
  });


  $('#audio').click(() => {
    $('#action-files').click();
  });

});
