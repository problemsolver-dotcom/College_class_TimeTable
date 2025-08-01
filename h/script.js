// Global variable to hold the timetable data once fetched.
let timetable = {};

/**
 * Returns an emoji icon based on the class type.
 * @param {string} type - The type of the class (e.g., 'Lecture', 'Lab').
 * @returns {string} An emoji representing the class type.
 */
function getTypeIcon(type) {
    const icons = {
        'Lecture': '📖',
        'Tutorial': '✏️',
        'Lab': '🔬'
    };
    return icons[type] || '📚'; // Default icon
}

/**
 * Renders the schedule for the currently selected day in the dropdown.
 */
function updateSchedule() {
    const daySelect = document.getElementById('daySelect');
    const container = document.getElementById('schedule-container');

    // Exit if essential elements aren't found
    if (!daySelect || !container) {
        console.error("Required DOM elements (daySelect or schedule-container) not found.");
        return;
    }
    
    const selectedDay = daySelect.value;
    const classes = timetable[selectedDay] || [];

    // Handle case where there are no classes for the selected day
    if (classes.length === 0) {
        container.innerHTML = `
            <div class="no-classes">
                <div class="no-classes-icon">🎉</div>
                <h3>It's a Free Day!</h3>
                <p>No classes are scheduled for ${selectedDay}. Enjoy your break!</p>
            </div>
        `;
        return;
    }

    // Build the HTML for the timeline view
    const timelineHTML = classes.map((classItem, index) => `
        <div class="timeline-item" style="animation-delay: ${index * 0.1}s">
            <div class="timeline-dot"></div>
            <div class="class-card" tabindex="0">
                <h2 class="subject-name">${classItem.subject}</h2>
                <div class="class-meta">
                    <div class="meta-badge type">
                        <span class="meta-icon" aria-hidden="true">${getTypeIcon(classItem.type)}</span>
                        <span>${classItem.type}</span>
                    </div>
                    <div class="meta-badge time">
                        <span class="meta-icon" aria-hidden="true">⏰</span>
                        <span>${classItem.time}</span>
                    </div>
                    <div class="meta-badge location">
                        <span class="meta-icon" aria-hidden="true">📍</span>
                        <span>${classItem.location}</span>
                    </div>
                </div>
            </div>
        </div>
    `).join('');

    container.innerHTML = `<div class="timeline">${timelineHTML}</div>`;
}

/**
 * Toggles the theme (placeholder function).
 */
function toggleTheme() {
    const button = document.querySelector('.theme-toggle');
    if (!button) return;
    
    // This is a placeholder. A full implementation would toggle a class on the <html> or <body> tag.
    const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDarkMode) {
        document.documentElement.setAttribute('data-theme', 'light');
        button.innerHTML = '🌙 Dark Mode';
        // Here you would update CSS variables for the light theme.
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        button.innerHTML = '☀️ Light Mode';
    }
    console.log("Theme toggled. (This is a visual placeholder)");
}


/**
 * Initializes the application after the DOM is fully loaded.
 */
document.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('schedule-container');
    const daySelect = document.getElementById('daySelect');

    try {
        // Show a loading state
        if (container) container.innerHTML = '<p style="text-align: center;">Loading schedule...</p>';

        // Fetch timetable data from the backend API
        const response = await fetch('/api/timetable');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        timetable = await response.json();

        // Set the dropdown to the current day passed from the server
        const currentDay = document.body.dataset.currentDay;
        if (daySelect && currentDay && timetable.hasOwnProperty(currentDay)) {
            daySelect.value = currentDay;
        }

        // Render the initial schedule
        updateSchedule();

    } catch (error) {
        console.error('Failed to fetch or process timetable data:', error);
        if (container) {
            container.innerHTML = `
                <div class="no-classes">
                    <div class="no-classes-icon">⚠️</div>
                    <h3>Oops! Something went wrong.</h3>
                    <p>We couldn't load the schedule. Please try refreshing the page.</p>
                </div>
            `;
        }
    }

    // Add keyboard navigation for switching days with arrow keys
    document.addEventListener('keydown', (e) => {
        if (!daySelect) return;
        if (e.target === daySelect) return; // Don't interfere with select's native controls

        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            e.preventDefault(); // Prevent browser back/forward navigation
            const currentIndex = daySelect.selectedIndex;
            const numOptions = daySelect.options.length;
            let newIndex;

            if (e.key === 'ArrowLeft') {
                newIndex = (currentIndex - 1 + numOptions) % numOptions;
            } else { // ArrowRight
                newIndex = (currentIndex + 1) % numOptions;
            }
            
            daySelect.selectedIndex = newIndex;
            updateSchedule();
        }
    });
});
