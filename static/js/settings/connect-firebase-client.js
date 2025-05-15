<<<<<<< HEAD
let userEmail = localStorage.getItem("user_email");

document.getElementById("connect-firebase").addEventListener("click", async () => {
  const firebaseConfig = window.firebaseConfig; // 👈 recupera do global

  if (!firebaseConfig) {
    return alert("Por favor, selecione o JSON de configuração Firebase primeiro.");
  }

  if (!userEmail) {
    alert("Sessão expirada ou e-mail não encontrado. Faça login novamente.");
    return window.location.href = "https://softwareai.rshare.io/login";
  }

  await fetch("https://softwareai.rshare.io/api/save-firebase-config", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: userEmail, config: firebaseConfig }),
  });

  document.getElementById("firebase-connected-status").textContent = `Conectado como ${userEmail}`;
  document.getElementById("firebase-connected-status").classList.replace("text-yellow-400", "text-green-400");
});
=======
let userEmail = localStorage.getItem("user_email");

document.getElementById("connect-firebase").addEventListener("click", async () => {
  const firebaseConfig = window.firebaseConfig; // 👈 recupera do global

  if (!firebaseConfig) {
    return alert("Por favor, selecione o JSON de configuração Firebase primeiro.");
  }

  if (!userEmail) {
    alert("Sessão expirada ou e-mail não encontrado. Faça login novamente.");
    return window.location.href = "https://softwareai.rshare.io/login";
  }

  await fetch("https://softwareai.rshare.io/api/save-firebase-config", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: userEmail, config: firebaseConfig }),
  });

  document.getElementById("firebase-connected-status").textContent = `Conectado como ${userEmail}`;
  document.getElementById("firebase-connected-status").classList.replace("text-yellow-400", "text-green-400");
});
>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
