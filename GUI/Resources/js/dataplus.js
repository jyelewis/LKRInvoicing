dataplus = {};

dataplus.chooseRow = function(tableName, callback){
	var modalURL = "/table/" + encodeURIComponent(tableName) + "?Select=1&Modal=1";
	$.fancybox({
			'padding'		: 20,
			'autoScale'		: true,
			'width'			: '75%',
			'height'		: '90%',
			'fitToView'   : false,
			'autoSize'    : false,
			'href'			: modalURL,
			'type'			: 'iframe',
		});
	selectRowModalCallback = function(id){
		$.fancybox.close();
		callback(id);
		selectRowModalCallback = null;
	};
}

dataplus.viewRow = function(tableName, rowID){
	if (window.self !== window.top) {
		window.top.dataplus.viewRow(tableName, rowID);
		return false;
	}
	var modalURL = "/table/" + encodeURIComponent(tableName) + "/row/" + encodeURIComponent(rowID) + '/view';
	$.fancybox({
		'padding'		: 20,
		'autoScale'		: true,
		'width'			: '75%',
		'height'		: '90%',
		'fitToView'   : false,
		'autoSize'    : false,
		'href'			: modalURL,
		'type'			: 'iframe',
	});
}

$(document).ready(function(){
	$(".ckeditor").ckeditor();
});

