$('.form-control').removeClass('input');
$('#id_CD, #id_CL, #id_Wu_, #id_L, #id_b, #id_h, #id_phi, #id_ec, #id_rec, #id_agg, #id_cuan, #id_pbar').each(function () {
    if ($(this).val() != '') {
        $(this).addClass('input');
    }})
$('#group-y').hide();

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

$("#id_carga").change(function(){
    if ($("#id_carga").val() == "1") {
        $('#id_CD').show();
        $('#group-CD').show();
        $('#id_CD').attr('required', '');
        $('#id_CD').attr('data-error', 'This field is required.');

        $('#id_CL').show();
        $('#group-CL').show();
        $('#id_CL').attr('required', '');
        $('#id_CL').attr('data-error', 'This field is required.');

        $('#id_Wu_').hide();
        $('#group-Wu_').hide();
        $('#id_Wu_').removeAttr('required');
        $('#id_Wu_').removeAttr('data-error');

        $('p#show-cdcl').show();
        $("#group-CD").before('<div id="cargas"></div>');
        $("#cargas").append($("#group-CD"), $("#group-CL"));
        $("#cargas").addClass("d-flex flex-wrap");
        $("#group-CD, #group-CL").addClass('d-flex align-items-end mb-4');

    }   else {
    if ($("#id_carga").val() == "2") {
        $('#id_CD').hide();
        $('#group-CD').hide();
        $('#id_CD').removeAttr('required');
        $('#id_CD').removeAttr('data-error');

        $('#id_CL').hide();
        $('#group-CL').hide();
        $('#id_CL').removeAttr('required');
        $('#id_CL').removeAttr('data-error');

        $('#id_Wu_').show();
        $('#group-Wu_').show();
        $('#id_Wu_').attr('required', '');
        $('#id_Wu_').attr('data-error', 'This field is required.');

        $('p#show-cdcl').hide();
        $("#group-CD, #group-CL").removeClass('d-flex align-items-end mb-4');
        $("#cargas").removeClass("d-flex flex-wrap");
            
    }   else {
        $('#id_CD').hide();
        $('#group-CD').hide();
        $('#id_CD').removeAttr('required');
        $('#id_CD').removeAttr('data-error');

        $('#id_CL').hide();
        $('#group-CL').hide();
        $('#id_CL').removeAttr('required');
        $('#id_CL').removeAttr('data-error');

        $('#id_Wu_').hide();
        $('#group-Wu_').hide();
        $('#id_Wu_').removeAttr('required');
        $('#id_Wu_').removeAttr('data-error');

        $("#group-CD, #group-CL").removeClass('d-flex align-items-end mb-4');
        $("#cargas").removeClass("d-flex flex-wrap");

        }
        
    }
  });

  $("#id_carga").trigger("change");


  



if (($('#y_r').length != 0 ) && ($('#y_r').val() != 'None') && ($('#y_r').val() != '') && ($('#y_r').val() != '0')) {
    $('#id_y').val($('#y_r').val())
}



if ($('#check-cuantia').length == 0 ) {
    $('#id_cuan').hide();
    $('#group-cuan').hide();
    $('#id_cuan').removeAttr('required');
    $('#id_cuan').removeAttr('data-error');

    $('#id_pbar').hide();
    $('#group-pbar').hide();
    $('#id_pbar').removeAttr('required');
    $('#id_pbar').removeAttr('data-error');

}   else {    
if (($('#id_op_cuantia').val() == '1' ) && ($('#id_op_acero').val() == '1')) {
    if (($('#primera').val() == '') || ($('#primera').val() == 'None')) {
        $('#id_cuan').show();
        $('#group-cuan').show();
        $('#id_cuan').attr('required', '');
        $('#id_cuan').attr('data-error', 'This field is required.');
        
        $('p#show-t').show();
        $('p#show-f').hide();

        $('#id_pbar').hide();
        $('#group-pbar').hide();
        $('#id_pbar').removeAttr('required');
        $('#id_pbar').removeAttr('data-error');
        
        $('p#show-manual').hide();
        $('p#show-auto').hide();

    }   else {
        $('#id_cuan').show();
        $('#group-cuan').show();
        $('#id_cuan').attr('required', '');
        $('#id_cuan').attr('data-error', 'This field is required.');
        
        $('p#show-t').show();
        $('p#show-f').hide();

        $('#id_pbar').show();
        $('#group-pbar').show();
        $('#id_pbar').attr('required', '');
        $('#id_pbar').attr('data-error', 'This field is required.');

        $('p#show-manual').show();
        $('p#show-auto').hide();
    }
}   else {
if (($('#id_op_cuantia').val() == '1' ) && ($('#id_op_acero').val() == '2')) {
    $('#id_cuan').show();
    $('#group-cuan').show();
    $('#id_cuan').attr('required', '');
    $('#id_cuan').attr('data-error', 'This field is required.');
    
    $('p#show-t').show();
    $('p#show-f').hide();

    $('#id_pbar').hide();
    $('#group-pbar').hide();
    $('#id_pbar').removeAttr('required');
    $('#id_pbar').removeAttr('data-error');
    
    $('p#show-manual').hide();
    
    if ($('#primera').val() == '') {
        $('p#show-auto').hide();
    }   else {
        $('p#show-auto').show();
    }
}   else {
if (($('#id_op_cuantia').val() == '2' ) && ($('#id_op_acero').val() == '1')) {
    $('#id_cuan').hide();
    $('#group-cuan').hide();
    $('#id_cuan').removeAttr('required');
    $('#id_cuan').removeAttr('data-error');

    $('p#show-t').hide();
    $('p#show-f').show();

    $('#id_pbar').show();
    $('#group-pbar').show();
    $('#id_pbar').attr('required', '');
    $('#id_pbar').attr('data-error', 'This field is required.');

    $('p#show-manual').show();
    $('p#show-auto').hide();
}   else {
if (($('#id_op_cuantia').val() == '2' ) && ($('#id_op_acero').val() == '2')) {
    $('#id_cuan').hide();
    $('#group-cuan').hide();
    $('#id_cuan').removeAttr('required');
    $('#id_cuan').removeAttr('data-error');

    $('p#show-t').hide();
    $('p#show-f').show();

    $('#id_pbar').hide();
    $('#group-pbar').hide();
    $('#id_pbar').removeAttr('required');
    $('#id_pbar').removeAttr('data-error');

    $('p#show-manual').hide();
    $('p#show-auto').show();
}}}}}

$('p#break_cuantia').hide();
$('div#break_cuantia').hide();
if (($('#id_cuantia').val() != 'None') && ($('#id_cuantia').val() != '')) {
    $('p#break_cuantia').show();
    $('div#break_cuantia').show();   
}
$('div#break_acero').hide();
if (($('input#id-barra').val() != "None") && ($('input#id-barra').val() != '')) {
    $('div#break_acero').show();
    $('#check-acero').val('check'); 
}

$("#group-L").before('<div class="d-flex flex-wrap" id="sm"></div>');
$("#sm").append($("#group-L"), $("#group-b"), $("#group-h"), $("#group-phi"), $("#group-ec"), $("#group-rec"));
$("#group-L, #group-b, #group-h, #group-phi, #group-ec, #group-rec").addClass('d-flex align-items-end mb-4');

$('div.step-number').addClass('vigas');

$( "label input" ).click(function() {
    $( "p.onoff" ).toggle();
  });