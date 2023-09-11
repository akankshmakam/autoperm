document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("permission-form");
    const downloadJpgButton = document.getElementById("download-jpg");
    const downloadPdfButton = document.getElementById("download-pdf");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const selectedNames = Array.from(form.querySelectorAll("input[type=checkbox]:checked"))
            .map(checkbox => checkbox.nextElementSibling.textContent);

        const startTime = form.querySelector("input[name=time]").value;
        const endTime = form.querySelector("input[name=time_end]").value;

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ selectedNames, startTime, endTime }),
        });

        if (response.ok) {
            const data = await response.json();
            const newWindow = window.open("", "_blank");
            newWindow.document.write(data.formattedDocument);
        }
    });

    downloadPdfButton.addEventListener("click", async function () {
        window.open("/generate/pdf", "_blank");
    });

    downloadJpgButton.addEventListener("click", async function () {
        window.open("/generate/jpg", "_blank");
    });
});
