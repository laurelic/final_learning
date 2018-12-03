d3.json("/drg_all").then(function(data) {
	var selector = d3.select("#selDrgDataset");
	console.log(data);
	data.forEach(function(d) {
		selector
			.append("option")
			.text(d['drg_definition'])
			.property("value", d['drg_id'] + '|'+ d['weights'] + '|' + d['geometric_mean_los'] + '|' + d['arithmetic_mean_los'] + '|' + d['drg_definition']);
	});
	const firstSample = data[0];
});


d3.json("/hrr_all").then(function(data) {
	var selector = d3.select("#selHrrDataset");
	console.log(data);
	data.forEach(function(d) {
		selector
			.append("option")
			.text(d['hrr_description'])
			.property("value", d['hrr_id'] + '|' + d['hrr_description']);
	});
	const firstSample = data[0];
}); 


/*  
d3.json("/provider_all").then(function(data) {
	var selector = d3.select("#selProviderDataset");
	data.forEach(function(d) {
		selector
			.append("option")
			.text(d['provider_name'])
			.property("value", d['provider_rowid'] + '|' + d['provider_name']);
	});
	const firstSample = data[0];

});  */

function hrrReload( drg_definition ){
	console.log("reload Hrr function: " + drg_definition);
	// clear existing options before reload
	document.getElementById("selHrrDataset").options.length = 0;
	
	var path = "/hrr/" + drg_definition;
	console.log ("hrr path: " + path);
	
	d3.json(path).then(function(data) {
	var selector = d3.select("#selHrrDataset");
	console.log(data);
	data.forEach(function(d) {
		selector
			.append("option")
			.text(d['hrr_description'])
			.property("value", d['hrr_id'] + '|' + d['hrr_description']);
	});
	const firstSample = data[0];
}); 

};


// load providers with in the selected hrr  
function providerReload( hrr_description ){
	console.log("reload provider function: " + hrr_description);
	//var selector = d3.select("#selProviderDataset");
	
	// clear existing options before reload
	document.getElementById("selProviderDataset").options.length = 0;
	
	var path = "/provider/" + hrr_description;
	
	d3.json(path).then(function(data) {
		console.log("json call");
		var selector = d3.select("#selProviderDataset");
		data.forEach(function(d) {
			selector
				.append("option")
				.text(d['provider_name'])
				.property("value", d['provider_rowid'] + '|' + d['provider_name']);
		});
		const firstSample = data[0];

	})
};



function drgOptionChanged(newSample) {
	var drg_sel = newSample;
	console.log('drg: ' + drg_sel);
/*
	var drg_arr = drg_sel.split("|");
	var drg_definition = drg_arr[4];
	console.log('drg_definition: '  + drg_definition);
	// reload hrr list to contain only hrr that performed the procedure
	hrrReload (drg_definition);
*/	
};

function hrrOptionChanged(newSample) {
	var hrr_sel = newSample;
	console.log ('hrr: ' + hrr_sel);
	var hrr_arr = hrr_sel.split("|");
	console.log('hrr_description: ' + hrr_arr[1]);
	var hrr_description = hrr_arr[1];
	providerReload( hrr_description );
	console.log("reload provider");
};

function providerOptionChanged(newSample) {
	var provider_sel = newSample;
	console.log('provider: ' + provider_sel);
};