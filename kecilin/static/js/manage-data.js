function showModalDelete(id, name) {
	var url = $("#modal_button_delete").attr('href');
	var newurl = url.split('/').slice(0,-1).join('/')+'/'+id
	$("#modal_button_delete").attr('href', newurl)
	modal_delete.showModal()
}