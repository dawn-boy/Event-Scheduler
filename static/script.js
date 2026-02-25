const API_URL = "https://event-scheduler-m4bj.onrender.com/events";

document.addEventListener("DOMContentLoaded", fetchEvents);

async function fetchEvents() {
    const response = await fetch(API_URL);
    const events = await response.json();
    window.currentEvents = events;

    const eventsList = document.getElementById("eventsList");
    eventsList.innerHTML = ""; 
    
    events.forEach(event => {
        const eventDiv = document.createElement("div");
        eventDiv.classList.add("event");

        eventDiv.innerHTML = `
            <div class="event-left">
                <p class="event-date">${new Date(event.event_date).toDateString()}</p>
                <p class="event-title">${event.title}</p>
                <p class="event-time">${new Date(event.event_date).toLocaleTimeString()}</p>
            </div>
            <div>
                <p class="event-place-title">Place</p>
                <p class="event-place">${event.description || "N/A"}</p>
            </div>
            <div class="event-right">
                <button onclick="editEvent(${event.id})">edit</button>
                <button onclick="deleteEvent(${event.id})">delete</button>
            </div>
        `;

        eventsList.appendChild(eventDiv);
    });
}

document.querySelector(".new-events-form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const title = document.getElementById("title").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const description = document.getElementById("description").value;

    const eventDate = `${date}T${time}:00`;

    if (editingId) {
        await fetch(`${API_URL}/${editingId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                title,
                event_date: eventDate,
                description: description
            })
        });

        editingId = null;
    } else {
        await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                title,
                event_date: eventDate,
                description: description 
            })
        });
    }

    fetchEvents();
    this.reset();
});

async function deleteEvent(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });

    fetchEvents();
}

let editingId = null;

function editEvent(id) {
    const event = window.currentEvents.find(e => e.id === id);

    if (!event) return;

    document.getElementById("title").value = event.title;

    const dt = new Date(event.event_date);
    document.getElementById("date").value = dt.toISOString().split("T")[0];
    document.getElementById("time").value = dt.toTimeString().slice(0,5);

    document.getElementById("description").value = event.description || "";

    editingId = id;
}

const dateInput = document.getElementById("date");
const dateError = document.getElementById("dateError");

dateInput.addEventListener("change", function () {

    const selectedDate = new Date(this.value);
    const today = new Date();

    today.setHours(0,0,0,0);

    if (selectedDate < today) {
        dateError.textContent = "Date cannot be in the past.";
        this.classList.add("invalid");
    } else {
        dateError.textContent = "";
        this.classList.remove("invalid");
    }
    document.getElementById("submit").disabled = selectedDate < today;
});