<<<<<<< HEAD

const agentSelectorModal = document.getElementById("agent-selector-modal-chat");
const openAgentSelectorBtn = document.getElementById("open-agent-selector");
const closeAgentSelectorBtn = document.getElementById("close-agent-selector");

openAgentSelectorBtn.addEventListener("click", () => {
    agentSelectorModal.classList.remove("hidden");
});

closeAgentSelectorBtn.addEventListener("click", () => {
    agentSelectorModal.classList.add("hidden");
});

// Fecha o modal se clicar fora
document.addEventListener("click", (e) => {
    if (!agentSelectorModal.contains(e.target) && !openAgentSelectorBtn.contains(e.target)) {
        agentSelectorModal.classList.add("hidden");
    }
});

=======

const agentSelectorModal = document.getElementById("agent-selector-modal-chat");
const openAgentSelectorBtn = document.getElementById("open-agent-selector");
const closeAgentSelectorBtn = document.getElementById("close-agent-selector");

openAgentSelectorBtn.addEventListener("click", () => {
    agentSelectorModal.classList.remove("hidden");
});

closeAgentSelectorBtn.addEventListener("click", () => {
    agentSelectorModal.classList.add("hidden");
});

// Fecha o modal se clicar fora
document.addEventListener("click", (e) => {
    if (!agentSelectorModal.contains(e.target) && !openAgentSelectorBtn.contains(e.target)) {
        agentSelectorModal.classList.add("hidden");
    }
});

>>>>>>> fee0a3f67f29d93c63fe941c1f545cb569adace2
