$(function () {

    $(document).on("click", "#btIncluir", function () {

        if (!$('#campoImagem').val()) {
            //e.preventDefault();
            alert('Please Upload File');
        }
        
        else {
            var dados_foto = new FormData($('#meuform')[0]);

            $.ajax({
                url: 'http://localhost:5000/save_image',
                method: 'POST',
                //dataType: 'json',
                data: dados_foto, // dados serão enviados em formato normal, para upload da foto
                contentType: false,
                cache: false,
                processData: false,
                success: function (data) {
                    alert("Parabéns a foto foi enviada!");
                },
                error: function (data) {
                    alert("vish sua foto não foi enviada");
                }
            });
        };
    });
});