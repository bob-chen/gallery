/*!
 * Copyright (c) 2015 Bob Chen
*/

Array.prototype.contains = function(item){
   return RegExp("\\b"+item+"\\b").test(this);
};

String.prototype.format = function(){
	var args = arguments;
	return this.replace(/\{(\d+)\}/g,
		function(m,i){
			return args[i];
	});
};


