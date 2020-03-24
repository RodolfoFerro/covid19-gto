// jQuery counterUp (used in cases section)
$('[data-toggle="counter-up"]').counterUp({
	delay: 10,
	time: 1000
});

// Tooltip for map
function showTooltip(evt, text) {
	let tooltip = document.getElementById("tooltip");
	tooltip.innerHTML = text;
	tooltip.style.display = "block";
	tooltip.style.left = evt.pageX;
	tooltip.style.top = evt.pageY;
}
  
function hideTooltip() {
	var tooltip = document.getElementById("tooltip");
	tooltip.style.display = "none";
}