// Ensure file loads after DOM is ready
document.addEventListener("DOMContentLoaded", async function () {

    // Select stat form from myself.html using getElementById
    const form = document.getElementById("stat-form");
    // Check form exists, if not, exit
    if (!form) return;

    // Else, add event listener for submitting form and override default form submission (e.g. page reload)
    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        // Package form data using FormData Object and save in variable
        const formData = new FormData(form);

        try {
            // Send form data to /myself route (mimics app.py POST route)
            const response = await fetch("/myself", {
                method: "POST",
                body: formData
            });

            // Wait for response and convert it to JSON
            const result = await response.json();

            // Check if the result is successful
            if (result.success) {
                // Update stats in the DOM
                document.getElementById("stat-watchful").textContent = result.new_stats.watchful;
                document.getElementById("stat-shadowy").textContent = result.new_stats.shadowy;
                document.getElementById("stat-dangerous").textContent = result.new_stats.dangerous;
                document.getElementById("stat-persuasive").textContent = result.new_stats.persuasive;
                document.getElementById("apprehensions").textContent = result.new_stats.apprehensions;

                // Update story text
                const storyDiv = document.getElementById("story-text");
                storyDiv.textContent = result.story_text;
                // Show the story div by removing the d-none class
                storyDiv.classList.remove("d-none");

                // Rebuild the amount dropdown menu
                const amountSelect = document.getElementById("amount-select");
                amountSelect.innerHTML = '<option value="" disabled selected>Select one</option>';

                // Populate the amount dropdown with options from 1 to the new number of apprehensions
                for (let i = 1; i <= result.new_stats.apprehensions; i++) {
                    const option = document.createElement("option");
                    option.value = i;
                    option.textContent = i;
                    amountSelect.appendChild(option);
                }

                // Reset form
                form.reset();
            } else {
                alert(result.error || "Unknown error occurred.");
            }
        } catch (err) {
            console.error("Error submitting form:", err);
            alert("An unexpected error occurred.");
        }
    });
});
