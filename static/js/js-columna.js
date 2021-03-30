$('.form-control').removeClass('input');
$('#id_Pu, #id_Mu, #id_b, #id_h, #id_dP, #id_rec, #id_agg, #id_cuan1, #id_cuan2, #id_cuan3').each(function () {
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

$('#paso-cuantia').hide();
if (($('#id_cuan1').val() != 0) || ($('#id_cuan2').val() != 0) || ($('#id_cuan3').val() != 0)) {
    $('#paso-cuantia').show();    
}

if ($('#check').length == 0 ) {
    $('#id_cuan1').hide();
    $('#group-cuan1').hide();
    $('#id_cuan1').removeAttr('required');
    $('#id_cuan1').removeAttr('data-error');

    $('#id_cuan2').hide();
    $('#group-cuan2').hide();
    $('#id_cuan2').removeAttr('required');
    $('#id_cuan2').removeAttr('data-error');

    $('#id_cuan3').hide();
    $('#group-cuan3').hide();
    $('#id_cuan3').removeAttr('required');
    $('#id_cuan3').removeAttr('data-error');

    $('#id_dist').hide();
    $('#group-dist').hide();
    $('#id_dist').removeAttr('required');
    $('#id_dist').removeAttr('data-error');

}   else {
    if ($('span#id_g1').text() == $('span#id_g2').text()) {
        $('#id_cuan1').hide();
        $('#group-cuan1').hide();
        $('#id_cuan1').removeAttr('required');
        $('#id_cuan1').removeAttr('data-error');
    
        $('#id_cuan2').hide();
        $('#group-cuan2').hide();
        $('#id_cuan2').removeAttr('required');
        $('#id_cuan2').removeAttr('data-error');
    
        $('#id_cuan3').show();
        $('#group-cuan3').show();
        $('#id_cuan3').attr('required', '');
        $('#id_cuan3').attr('data-error', 'This field is required.');

        $('#id_distribucion').show();
        $('#group-distribucion').show();
        $('#id_dist').attr('required', '');
        $('#id_dist').attr('data-error', 'This field is required.');

        $('p.showg').show();
        $('div.showg1g2').hide();
    
    }   else {
        $('#id_cuan1').show();
        $('#group-cuan1').show();
        $('#id_cuan1').attr('required', '');
        $('#id_cuan1').attr('data-error', 'This field is required.');
    
        $('#id_cuan2').show();
        $('#group-cuan2').show();
        $('#id_cuan2').attr('required', '');
        $('#id_cuan2').attr('data-error', 'This field is required.');
    
        $('#id_cuan3').hide();
        $('#group-cuan3').hide();
        $('#id_cuan3').removeAttr('required');
        $('#id_cuan3').removeAttr('data-error');
        
        $('#id_distribucion').show();
        $('#group-distribucion').show();
        $('#id_dist').attr('required', '');
        $('#id_dist').attr('data-error', 'This field is required.');

        $('p.showg').hide();
        $('div.showg1g2').show();
    }
};

if ($('.cuan-min').val() < '0.01' ) {
    $('.ver_min_T').hide();
    $('.ver_min_F').show();
}   else {
    $('.ver_min_T').show();
    $('.ver_min_F').hide();
}

$("#group-Pu").before('<div class="d-flex flex-wrap" id="sm"></div>');
$("#sm").append($("#group-Pu"), $("#group-Mu"), $("#group-b"), $("#group-h"), $("#group-dP"), $("#group-rec"));
$("#group-Pu, #group-Mu, #group-b, #group-h, #group-dP, #group-rec").addClass('d-flex align-items-end mb-4');

$('div.step-number').addClass('columnas');

$( "label input" ).click(function() {
    $( "p.onoff" ).toggle();
  });