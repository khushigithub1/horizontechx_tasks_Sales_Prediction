/* ==========================================================
   Sales Intelligence Dashboard
   Dashboard Animations
========================================================== */

// ==========================================================
// Page Loading Animation
// ==========================================================

window.addEventListener("load", function () {

    document.body.style.opacity = "0";

    document.body.style.transition = "opacity 0.8s ease";

    setTimeout(() => {

        document.body.style.opacity = "1";

    }, 150);

});

// ==========================================================
// Button Click Animation
// ==========================================================

document.addEventListener("click", function (e) {

    if (e.target.classList.contains("predict-btn")) {

        e.target.style.transform = "scale(0.95)";

        e.target.style.transition = "0.15s";

        setTimeout(() => {

            e.target.style.transform = "scale(1)";

        }, 150);

    }

});

// ==========================================================
// Card Hover Animation
// ==========================================================

window.addEventListener("load", () => {

    const observer = new MutationObserver(() => {

        const cards = document.querySelectorAll(".glass-card");

        cards.forEach(card => {

            card.onmouseenter = () => {

                card.style.transform = "translateY(-8px)";

                card.style.transition = "0.3s";

            };

            card.onmouseleave = () => {

                card.style.transform = "translateY(0px)";

            };

        });

    });

    observer.observe(document.body, {

        childList: true,

        subtree: true

    });

});

// ==========================================================
// Smooth Scroll
// ==========================================================

window.addEventListener("load", () => {

    document.documentElement.style.scrollBehavior = "smooth";

});

// ==========================================================
// Dashboard Loaded Notification
// ==========================================================

window.addEventListener("load", function () {

    console.log("🚀 Sales Intelligence Dashboard Loaded");

});

// ==========================================================
// Live Clock
// ==========================================================

function updateClock() {

    const clock = document.getElementById("live-clock");

    if (clock) {

        const now = new Date();

        clock.innerHTML = now.toLocaleString();

    }

}

setInterval(updateClock, 1000);

// ==========================================================
// Animated Number Counter
// ==========================================================

function animateValue(id, start, end, duration) {

    let obj = document.getElementById(id);

    if (!obj) return;

    let range = end - start;

    let current = start;

    let increment = end > start ? 1 : -1;

    let stepTime = Math.abs(Math.floor(duration / range));

    let timer = setInterval(function () {

        current += increment;

        obj.innerHTML = current;

        if (current == end) {

            clearInterval(timer);

        }

    }, stepTime);

}

// ==========================================================
// Ripple Effect
// ==========================================================

document.addEventListener("click", function (e) {

    if (e.target.tagName === "BUTTON") {

        const circle = document.createElement("span");

        const diameter = Math.max(e.target.clientWidth, e.target.clientHeight);

        circle.style.width = circle.style.height = `${diameter}px`;

        circle.style.left = `${e.offsetX - diameter / 2}px`;

        circle.style.top = `${e.offsetY - diameter / 2}px`;

        circle.classList.add("ripple");

        const ripple = e.target.getElementsByClassName("ripple")[0];

        if (ripple) {

            ripple.remove();

        }

        e.target.appendChild(circle);

    }

});

// ==========================================================
// Loading Animation for Prediction
// ==========================================================

document.addEventListener("click", function (e) {

    if (e.target.id === "predict-button") {

        e.target.innerHTML = "⏳ Predicting...";

        setTimeout(() => {

            e.target.innerHTML = "🚀 Predict Sales";

        }, 1200);

    }

});

// ==========================================================
// Welcome Toast
// ==========================================================

window.addEventListener("load", () => {

    setTimeout(() => {

        console.log("Welcome to Sales Intelligence Platform");

    }, 1000);

});