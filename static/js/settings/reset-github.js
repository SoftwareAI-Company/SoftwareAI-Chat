<<<<<<< HEAD
document.getElementById("reset-github").addEventListener("click", () => {
    if (!confirm("Tem certeza que deseja resetar a configuração do GitHub?")) return;
  
    fetch("https://softwareai.rshare.io/api/github/reset", {
      method: "POST",
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => {
        alert(data.message);
        location.reload();
      })
      .catch((err) => {
        console.error("Erro ao resetar GitHub:", err);
        alert("Erro ao tentar resetar GitHub.");
      });
  });
=======
document.getElementById("reset-github").addEventListener("click", () => {
    if (!confirm("Tem certeza que deseja resetar a configuração do GitHub?")) return;
  
    fetch("https://softwareai.rshare.io/api/github/reset", {
      method: "POST",
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => {
        alert(data.message);
        location.reload();
      })
      .catch((err) => {
        console.error("Erro ao resetar GitHub:", err);
        alert("Erro ao tentar resetar GitHub.");
      });
  });
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
  