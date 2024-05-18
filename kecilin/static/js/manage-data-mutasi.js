$('.button_add').on('click', function() {
	$('#modal_form_submit').trigger("reset");
	modal_form.showModal();
})

$('.button_edit').on('click', function() {
	var id = $(this).attr('data-id')

	var strObj = $(this).attr('data-object');
	jsonString = strObj.replace(/'/g, '"');
	object = JSON.parse(jsonString);
	
	$('#id_id').val(object.id);
	$('#id_nominal').val(object.nominal);	
	var date = new Date(object.datetime);
	var convert_date = date.toISOString().slice(0, 16);
	$('#id_datetime').val(convert_date).change();	
	$('#id_user_id').val(object.user_id).change();

	modal_form.showModal();
})

$('.button_delete').on('click', function() {
	var id = $(this).attr('data-id')
	var url = $("#modal_form_delete").attr('action');
	var newurl = url.split('/').slice(0,-1).join('/')+'/'+id
	$("#modal_form_delete").attr('action', newurl)
	modal_delete.showModal()
})