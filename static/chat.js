document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chat-form");
    const output = document.getElementById("output");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const prompt = document.getElementById("prompt").value;
        output.textContent = "";

        const formData = new FormData();
        formData.append("prompt", prompt);

        const res = await fetch("/api/generate", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        let text = data.response;

        // ✂️ Trim at the last complete sentence
        const lastEnd = Math.max(
            text.lastIndexOf("."),
            text.lastIndexOf("!"),
            text.lastIndexOf("?")
        );

        if (lastEnd !== -1) {
            text = text.substring(0, lastEnd + 1); // include the punctuation
        }

        // ⌨️ Animate character by character
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                output.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 5); // ~5ms between characters
            }
        }

        typeWriter();
    });
});
