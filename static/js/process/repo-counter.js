<<<<<<< HEAD
function atualizarContadorRepos() {
  const selecionados = document.querySelectorAll('input[name="github-repo"]:checked');
  const count = selecionados.length;
  const dropdownButton = document.getElementById("dropdownButton");
  if (dropdownButton) {
    dropdownButton.textContent = `Selected repositories: ${count} (for agent's knowledge)`;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("change", (event) => {
    if (event.target && event.target.name === "github-repo") {
      atualizarContadorRepos();
    }
  });

  atualizarContadorRepos();
});
=======
function atualizarContadorRepos() {
  const selecionados = document.querySelectorAll('input[name="github-repo"]:checked');
  const count = selecionados.length;
  const dropdownButton = document.getElementById("dropdownButton");
  if (dropdownButton) {
    dropdownButton.textContent = `Selected repositories: ${count} (for agent's knowledge)`;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("change", (event) => {
    if (event.target && event.target.name === "github-repo") {
      atualizarContadorRepos();
    }
  });

  atualizarContadorRepos();
});
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
