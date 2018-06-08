


const showFile = function(input, output) {
  console.log(output)
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(`#${output}`)
                .attr('src', e.target.result)
                .width(350)
        };

        reader.readAsDataURL(input.files[0]);
    }
}