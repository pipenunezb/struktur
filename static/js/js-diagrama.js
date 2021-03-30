$('.form-control').removeClass('input');
$('#id_F1, #id_F2, #id_F3, #id_F4, #id_F5, #id_F6, #id_B1, #id_B2, #id_B3, #id_B4, #id_B5, #id_B6, #id_b, #id_h, #id_rec, #id_E, #id_b1').each(function () {
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

$('.form-span.fc').removeClass('form-span');
$('.form-group.fc').prepend("<span class='label'>f'c </span>");
$('.form-span.fy').removeClass('form-span');
$('.form-group.fy').prepend('<span class="label">fy  </span>');

$('.form-control').attr('required', '');
$('.form-control').attr('data-error', 'This field is required.');

$('#id_F3, #id_F4, #id_F5, #id_F6, #id_B3, #id_B4, #id_B5, #id_B6').removeAttr('required');
$('#id_F3, #id_F4, #id_F5, #id_F6, #id_B3, #id_B4, #id_B5, #id_B6').removeAttr('data-error');

$("#group-F1").before('<div class="d-flex flex-wrap" id="sm"></div>');
$("#sm").append($("#group-F1"), $("#group-B1"), $("#group-F2"), $("#group-B2"), $("#group-F3"), $("#group-B3"), $("#group-F4"), $("#group-B4"), $("#group-F5"), $("#group-B5"), $("#group-F6"), $("#group-B6"), $("#group-b"), $("#group-h"));
$("#group-F1, #group-B1, #group-F2, #group-B2, #group-F3, #group-B3, #group-F4, #group-B4, #group-F5, #group-B5, #group-F6, #group-B6, #group-b, #group-h").addClass('d-flex align-items-end mb-4');

$("#group-E").before('<div class="d-flex flex-wrap" id="sm2"></div>');
$("#sm2").append($("#group-E"), $("#group-b1"));
$("#group-E, #group-b1").addClass('d-flex align-items-end mb-4');

$('div.step-number').addClass('diagramas');

if ($('#id_F3').val() == '0') {
    $('p#fila3').hide();
}
if ($('#id_F4').val() == '0') {
    $('p#fila4').hide();
}
if ($('#id_F5').val() == '0') {
    $('p#fila5').hide();
}
if ($('#id_F6').val() == '0') {
    $('p#fila6').hide();
}