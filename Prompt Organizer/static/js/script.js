// Dummy data representing the YAML structure
const tasks = {
    Task_1: {
        prompts: {
            version_1: {
                prompt: "",
                temperature: 0.1,
                // ... other properties ...
            },
            // ... other versions ...
        },
        // ... other properties ...
    },
    Task_2: {
        prompts: {
            version_1: {
                prompt: "",
                temperature: 0.1,
                // ... other properties ...
            },
            // ... other versions ...
        },
        // ... other properties ...
    },
    // ... other tasks ...
};

function displayTaskDetails() {
    const dropdown = document.getElementById("taskDropdown");
    const selectedTask = dropdown.value;
    const detailsDiv = document.getElementById("taskDetails");

    const task = tasks[selectedTask];
    if (!task) {
        detailsDiv.innerHTML = "Task details not found!";
        return;
    }

    let detailsHtml = "<h3>Details for " + selectedTask + "</h3>";

    for (const [key, value] of Object.entries(task)) {
        detailsHtml += "<h4>" + key + "</h4>";
        for (const [subKey, subValue] of Object.entries(value)) {
            detailsHtml += "<p>" + subKey + ": " + JSON.stringify(subValue, null, 2) + "</p>";
        }
    }

    detailsDiv.innerHTML = detailsHtml;
}
