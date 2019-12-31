function write(list) {
	
	var template = `
	<a href='$url' target='_blank'>
		<div class='col-xs-6 col-md-3 col-lg-2 item' style='background-image: url($img);'>
			<div class='col-xs-12 item-hover'>
				<h3>
					$name
					<br>
					<span class='item-price' style='float: right;'>
						<b>
						$website $price1 € / $price2 €
						</b>
					</span>
				</h3>
			</div>
		</div>
	</a>
	`;
//	var template = "<a href='$url' target='_blank'><div class='col-xs-6 col-md-3 col-lg-2 item' style='background-image: url('$img');'><div class='col-xs-12 item-hover'><h3>$name<br><span class='item-price' style='float: right;'><b>$website $price1 € / $price2 €</b></span></h3></div></div></a>";
	
	$(".items").empty();
	for (i = 0; i < list.length; i++) {
		var html = template;
		html = html.replace("$url", list[i]["url"]);
		html = html.replace("$name", list[i]["name"]);
		html = html.replace("$img", list[i]["img"]);
		html = html.replace("$price1", list[i]["price1"]);
		html = html.replace("$price2", list[i]["price2"]);
		html = html.replace("$website", list[i]["website"]);
		console.log(html);
		$(".items").append(html);
	}
}

function refresh() {
	if ($("#okidoki").is(':checked')) {
		var okidoki = true;
	} else {
		var okidoki = false;
	}
	if ($("#osta").is(':checked')) {
		var osta = true;
	} else {
		var osta = false;
	}
	if ($("#soov").is(':checked')) {
		var soov = true;
	} else {
		var soov = false;
	}
	if ($("#kuldnebors").is(':checked')) {
		var kuldnebors = true;
	} else {
		var kuldnebors = false;
	}
	var min = parseInt($("#min-price").val(),10);
	var max = parseInt($("#max-price").val(),10);
	var type = $("#filter").val();

	var list = [];

	// first set of filters
	for (i = 0; i < db.length; i++) {
		try {
			// price filters
			if (parseInt(db[i]["price1"],10) > min || parseInt(db[i]["price2"],10) > min) {
				if (parseInt(db[i]["price1"],10) < max || parseInt(db[i]["price2"],10) < max) {
					// website filters
					if (db[i]["website"] == "OKIDOKI" && okidoki) {
						list.push(db[i]);
					} else if (db[i]["website"] == "SOOV" && soov) {
						list.push(db[i]);
					} else if (db[i]["website"] == "OSTA" && osta) {
						list.push(db[i]);
					} else if (db[i]["website"] == "KULDNEBORS" && kuldnebors) {
						list.push(db[i]);
					}
				}
			}
		} catch(error) {
			// do nothing
		}
	}

	for (i = 0; i < list.length; i++) {
		if (list[i]["price1"] == "-") {
			list[i]["price1"] = 0;
		}
		if (list[i]["price2"] == "-") {
			list[i]["price2"] = 0;
		}
	}
	console.log(list[0]["price1"]);
	console.log(list[0]["price2"]);
	console.log(Math.max(list[0]["price1"],list[0]["price2"]));
	// sort filtering
	if (type == "no-filter") {
		// do nothing
	} else if (type == "l-2-h") {
		list.sort((a,b) => (Math.max(parseInt(a["price1"],10),parseInt(a["price2"],10))) < Math.max(parseInt(b["price1"],10),parseInt(b["price2"],10)) ? -1 : 1);
	} else if (type == "h-2-l") {
		list.sort((a,b) => (Math.max(parseInt(a["price1"],10),parseInt(a["price2"],10))) < Math.max(parseInt(b["price1"],10),parseInt(b["price2"],10)) ? 1 : -1);
	} else if (type == "a-2-z") {
		list.sort((a,b) => (a["name"] < b["name"]) ? -1 : 1 );
	} else if (type == "z-2-a") {
		list.sort((a,b) => (a["name"] < b["name"]) ? 1 : -1 );
	}



	write(list);
}
// init

write(db);