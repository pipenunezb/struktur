$('.form-control').removeClass('input');
$('#id_b, #id_h, #id_rec, #id_agg, #id_cuantia').each(function () {
    if ($(this).val() != '') {
        $(this).addClass('input');
    }})

$('.form-control').each(function () {
    $(this).on('click', function () {
        $(this).after().addClass('input');
    })
    $(this).on('blur', function () {
        if ($(this).val().trim() != "") {
            $(this).addClass('input');
        } else {
            $(this).removeClass('input');
        }
    })
})

$('.form-span.element').removeClass('form-span');
$('.form-group.element').prepend('<span class="label">Elemento  </span>');


$('.form-control').attr('required', '');
$('.form-control').attr('data-error', 'This field is required.');

if ($("#id_element").val() == '1') {
    $("p#viga").show();
    $("p#col").hide();
}   else {
    $("p#viga").hide();
    $("p#col").show();
}

$('div.step-number').addClass('acero');
