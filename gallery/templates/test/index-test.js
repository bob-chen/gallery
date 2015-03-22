QUnit.module("Common Test", {
	setup: function(){
		console.log("Test setup");
	},
	teardown: function(){
		console.log("Test teardown");
	}
});
QUnit.test( "Test String.format", function( assert ) {
	var tmpl1 = "hello {0}",
		tmpl2 = "a{1}b{0}",
		except1 = "hello world",
		except2 = "a1b0";
	assert.equal( tmpl1.format("world"), except1, "String.format ok." );
	assert.equal( tmpl2.format(0, 1), except2, "String.format ok." );
});
QUnit.test( "Test Array.contains", function( assert ) {
	var arr = [1,2,3, "a", "b"];
	assert.equal( arr.contains(1), true, "Array.contains ok." );
	assert.equal( arr.contains(4), false, "Array.contains ok." );
	assert.equal( arr.contains("a"), true, "Array.contains ok." );
	assert.equal( arr.contains("c"), false, "Array.contains ok." );
});


QUnit.module("AjaxClient Test", {
	setup: function(){
		console.log("Test setup");
	},
	teardown: function(){
		console.log("Test teardown");
	}
});

// an async test
QUnit.asyncTest("Test AjaxClient", 1, function(assert) {
    ajaxClient.loadData("/getPhotos/","GET", {page:1, prePage:1}, 
		function(data){
    		QUnit.start();	
    		assert.ok(true);
		}
    );
});


