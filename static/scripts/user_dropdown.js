
document.addEventListener("DOMContentLoaded", function () {
	const icon = document.getElementById("userIcon");
	const menu = document.getElementById("userDropdownMenu");

	// Toggle dropdown manually
	icon.addEventListener("click", function (e) {
		e.preventDefault();
		menu.classList.toggle("show");
	});

	// Optional: click outside to close
	document.addEventListener("click", function (e) {
		if (!icon.contains(e.target) && !menu.contains(e.target)) {
			menu.classList.remove("show");
		}
	});
});
