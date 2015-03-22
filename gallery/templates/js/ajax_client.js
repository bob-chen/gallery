/*!
 * This file is part of the DockerGUI software
 * Copyright (c) 2014 Alex Zhong, Bob Chen
 * 
 * License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
*/

function AjaxClient(){
	
	this.loadData = function(url, method, params, callback){
		$.ajax({
			url: url,
			type: method,
			data: params,
			dataType: 'json',
			complete: function(xhr, textStatus){

			},
			success: function(data, textStatus){
				console.log(textStatus);
				console.log(data);
				callback(data);
			}
		});
	};	
}

var ajaxClient = new AjaxClient();