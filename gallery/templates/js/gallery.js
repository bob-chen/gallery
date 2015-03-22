var glbFileData = null;

var _ready = false;
$(document).ready(function(){
  if(_ready){
	  return;
  }
  _ready = true;
  
  console.log("document ready");
  var container = $('#photoContainer');
  container.masonry({
    itemSelector : '.item',  
    columnWidth : "#container .item",
    gutter : 10,
  }); 

  var img = $('img', container),  
  	  imgCount = img.length; 
  
  img.load(function(){ 
	  imgCount -= 1;  
	  if(imgCount==0){
		  container.masonry();
	  }
  }); 

  $("#addBtn").click(function(){
	  initModal();
	  $("#modalAlert").modal('show');
  });

  
  $("#fileuploadBtn").click(function(){
  	$("#fileupload").click();
  });
  $("#fileupload").fileupload({
  	url: '/addPhoto/',
  	dataType: 'json',
  	//formData: {"a":'1', "b":'2'},
  	add: function(e, data){
  		//console.log(data);
  		var fileName = data.files[0].name;
  		$("#fileName").text(fileName);
  		//$("#fileupload").fileupload('option', 'formData', {"a":"123123"});
  		//data.submit();
  		glbFileData = data;
  	},
  	progressall: function(e, data){
  		var progress = parseInt(data.loaded / data.total *100, 10);

  		$("#progress").text(progress + "%");
  		$("#progress").attr("aria-valuenow", progress+"");
  		$("#progress").attr("style","width:{0}%".format(progress));    		
  	},
  	done: function(e, data){
  		console.log(data.result);
  		if(data.result.errorcode == 0){
  			finishCall(data.result);
  		} else {
  			$("#progress").addClass("progress-bar-danger");
  			$("#progress").text(data.result.errormsg);
  		}
  	}
  });
  
  $("#photoType").change(function(){
	  var photoType = $(this).val(),
	  	  fileGroup = $("#fileGroup"),
	  	  urlGroup = $("#urlGroup");
	  if(photoType === "url"){
		  fileGroup.hide();
		  urlGroup.show();
	  } else {
		  fileGroup.show();
		  urlGroup.hide();
	  }
  });
  
  $("#toUpload").click(function(){
	  var title = $.trim($("#inputTitle").val()),
	  	  comment = $.trim($("#inputComment").val()),
	  	  photoType = $("#photoType").val(),
	  	  url = $.trim($("#inputUrl").val());
	  
	  if(photoType === "url"){
		  ajaxClient.loadData('/addPhoto/', "POST", 
				  {title: title, comment: comment, isUrl: "true", url: url},
				  function(jsondata){
					  finishCall(jsondata); 
				  }
		  );
	  } else {
		  $("#fileupload").fileupload('option', 'formData',
			  {title: title, comment: comment, isUrl: "false"}
		  );
		  $(".progress").show();
		  glbFileData.submit();
	  }
  });
  
	$(window).scroll(function (){  
		var winScroll = document.documentElement.scrollTop || document.body.scrollTop;
		var winHeight= document.documentElement.clientHeight || document.body.clientHeight;
		var scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
		
		// scroll to the bottom
		if(scrollHeight == winScroll + winHeight){
			loadMorePhoto(container);
		}
	}); 

});  

function initModal()
{
	$("#inputTitle").val("");
	$("#inputComment").val("");
	$("#inputUrl").val("");
	$("#photoType").val("localFile");
	$("#fileGroup").show();
 	$("#urlGroup").hide();
	$(".progress").hide();
}

function finishCall(jsondata)
{
	if(jsondata.errorcode == 0){
		setTimeout(function(){
			window.location.reload();
		}, 1000);
	} else {
		$("#modalAlert .err").text(jsondata.errormsg);
	} 
}

var page = 1, prePage = 5,
	morePage = true;
function loadMorePhoto(container)
{
	if( !morePage){
		return;
	}
	page += 1;
	ajaxClient.loadData('/getPhotos/', "GET",
			{page: page, prePage: prePage},
			function(jsondata){
				if(jsondata.errorcode == 0){
					var photoList = jsondata.photoList;
					if(photoList.length == 0){
						morePage = false;
					}
					addItems(container, photoList);
				} else {
					console.log(jsondata.errmsg);
				}
			}
	);
}

function addItems(container, photoList)
{
	var msnry = container.data("masonry"),
		htmlTmpl = '<div class="item"><div class="item-content">' +
			'<h2>{0}</h2><a href="{1}" class="thumb"><img src="{1}" width="{2}" height="{3}"></a>' +
			'<div class="item-text">{4}</div>' +
			'</div></div>';
		html = "";
			
	for(var i=0, len=photoList.length; i < len; i+=1){
		var photoItem = photoList[i];
		html += htmlTmpl.format(photoItem["title"], photoItem["imageUrl"], photoItem["width"],
								photoItem["height"], photoItem["comment"]);
	}
  	var elem = $(html);
  	container.append(elem).masonry('appended', elem);
}

