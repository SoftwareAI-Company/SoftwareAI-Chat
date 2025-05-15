<<<<<<< HEAD

const modal = document.getElementById("custom-modal");
const plusBtn = document.getElementById("open-custom-modal");

// Toggle do modal
plusBtn.addEventListener("click", () => {
modal.classList.toggle("hidden");
});

// Fecha o modal se clicar fora
document.addEventListener("click", (e) => {
if (!modal.contains(e.target) && !plusBtn.contains(e.target)) {
    modal.classList.add("hidden");
}
});
=======

const modal = document.getElementById("custom-modal");
const plusBtn = document.getElementById("open-custom-modal");

// Toggle do modal
plusBtn.addEventListener("click", () => {
modal.classList.toggle("hidden");
});

// Fecha o modal se clicar fora
document.addEventListener("click", (e) => {
if (!modal.contains(e.target) && !plusBtn.contains(e.target)) {
    modal.classList.add("hidden");
}
});
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
