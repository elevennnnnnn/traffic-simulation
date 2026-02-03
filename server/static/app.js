const out = document.getElementById("out");
const btn = document.getElementById("btn");

btn.addEventListener("click", async () => {
    const res = await fetch("/api/ping", {method: "POST"});
    const data = await res.json();
    out.textContent = JSON.stringify(data, null, 2);
});

