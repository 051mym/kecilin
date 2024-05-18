$('.button_add').on('click', function() {
	$('#modal_form_submit').trigger("reset");
	modal_form.showModal();
})

$('.button_edit').on('click', function() {
	var id = $(this).attr('data-id')

	if (id) {
		var url = $("#modal_form_submit").attr('action');
		var newurl = url.split('/').slice(0,-1).join('/')+'/'+id
		$("#modal_form_submit").attr('action', newurl)
	}

	var strObj = $(this).attr('data-object');
	jsonString = strObj.replace(/'/g, '"');
	object = JSON.parse(jsonString);
	
	$('#id_id').val(object.id);
	$('#id_username').val(object.username);
	$('#id_email').val(object.email);	

	modal_form.showModal();
})

$('.button_delete').on('click', function() {
	var id = $(this).attr('data-id')
	var url = $("#modal_form_delete").attr('action');
	var newurl = url.split('/').slice(0,-1).join('/')+'/'+id
	$("#modal_form_delete").attr('action', newurl)
	modal_delete.showModal()
})