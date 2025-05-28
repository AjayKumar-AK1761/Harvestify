// user_dropdown.js - Robust, clean, production-ready
'use strict';

document.addEventListener("DOMContentLoaded", function () {
	const icon = document.getElementById("userIcon");
	const menu = document.getElementById("userDropdownMenu");
	if (!icon || !menu) return;

	// Toggle dropdown manually
	icon.addEventListener("click", function (e) {
		e.preventDefault();
		menu.classList.toggle("show");
		if (menu.classList.contains("show")) {
			menu.setAttribute('aria-expanded', 'true');
			icon.setAttribute('aria-expanded', 'true');
		} else {
			menu.setAttribute('aria-expanded', 'false');
			icon.setAttribute('aria-expanded', 'false');
		}
	});

	// Click outside to close
	document.addEventListener("click", function (e) {
		if (!icon.contains(e.target) && !menu.contains(e.target)) {
			menu.classList.remove("show");
			menu.setAttribute('aria-expanded', 'false');
			icon.setAttribute('aria-expanded', 'false');
		}
	});

	// Keyboard accessibility: close on Escape
	document.addEventListener("keydown", function (e) {
		if (e.key === "Escape") {
			menu.classList.remove("show");
			menu.setAttribute('aria-expanded', 'false');
			icon.setAttribute('aria-expanded', 'false');
		}
	});
});
