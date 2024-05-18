function showModalDelete(id, name) {
	var url = $("#modal_form_delete").attr('action');
	var newurl = url.split('/').slice(0,-1).join('/')+'/'+id
	$("#modal_form_delete").attr('action', newurl)
	console.log('a');
	modal_delete.showModal()
}

function showModalForm(data) {
	var mydata = JSON.parse(data);
	console.log(mydata);
	modal_form.showModal()
}