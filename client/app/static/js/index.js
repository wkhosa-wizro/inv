jQuery(function(){
    var counter = 1;
    jQuery('a.add-payment').click(function(event){
        event.preventDefault();

        var newRow = jQuery(
	'<hr><br>' +
        '<div>' +
        		'<label for="description">Description</lable>' +
        		'<textarea id="description" name="description'+ counter + '" ></textarea>' +
        '</div>' +
        '<div>' +
        		'<label for="price">Price</lable>' +
        		'<input type="number" id="price" name="price' + counter + '">' +
        '</div>' +
        '<div>' +
        		'<label for="Qty">Qty</label>'+
            '<input type="number" id="qty" name="qty' + counter + '">' +
        '</div>');
            counter++;
        jQuery('div.payment-details').append(newRow);
	console.log("ok....");

    });
});
