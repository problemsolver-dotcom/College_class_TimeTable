let timetable = {};

/* ---------- Icons ---------- */
function getTypeIcon(type) {
    const icons = {
        'Lecture': '📖',
        'Tutorial': '✏️',
        'Lab': '🔬'
    };
    return icons[type] || '📚';
}

/* ---------- Schedule Update ---------- */
function updateSchedule() {
    const daySelect = document.getElementById('daySelect');
    const container = document.getElementById('schedule-container');

    if (!daySelect || !container) return;

    const selectedDay = daySelect.value;
    const classes = timetable[selectedDay] || [];

    if (classes.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="icon">🎉</div>
                <h2>No Classes Today</h2>
                <p>Relax and recharge! Enjoy your day off.</p>
            </div>
        `;
        return;
    }

    container.innerHTML = classes.map((cls, i) => `
        <div class="class-entry fade-in" style="animation-delay: ${i * 0.1}s">
            <div class="time">${cls.time}</div>
            <div class="details">
                <h3>${cls.subject}</h3>
                <p>${getTypeIcon(cls.type)} ${cls.type} | 📍 ${cls.location}</p>
            </div>
        </div>
    `).join('');
}

/* ---------- Theme Toggle ---------- */
function setTheme(theme) {
    const html = document.documentElement;
    const button = document.querySelector('.theme-toggle');

    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    if (button) {
        button.textContent = theme === 'dark'
            ? '🌙 Dark Mode'
            : '☀️ Light Mode';
    }
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'dark';
    setTheme(current === 'dark' ? 'light' : 'dark');
}

/* ---------- Init ---------- */
document.addEventListener('DOMContentLoaded', async () => {
    const daySelect = document.getElementById('daySelect');
    const container = document.getElementById('schedule-container');
    const themeButton = document.querySelector('.theme-toggle');

    /* ----- Theme Init ----- */
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    if (themeButton) {
        themeButton.addEventListener('click', toggleTheme);
    }

    /* ----- Load Timetable ----- */
    try {
        container.innerHTML = '<p class="loading">Loading your schedule...</p>';
        const response = await fetch('/api/timetable');
        timetable = await response.json();

        const today = document.body.dataset.currentDay;
        if (timetable[today]) {
            daySelect.value = today;
        }

        updateSchedule();
    } catch (err) {
        console.error(err);
        container.innerHTML =
            '<p class="error">Failed to load timetable. Try refreshing.</p>';
    }

    /* ----- Day Change ----- */
    daySelect.addEventListener('change', updateSchedule);

    /* ----- Keyboard Navigation ----- */
    document.addEventListener('keydown', e => {
        if (e.target === daySelect) return;

        const index = daySelect.selectedIndex;
        if (e.key === 'ArrowLeft') {
            daySelect.selectedIndex =
                (index - 1 + daySelect.length) % daySelect.length;
            updateSchedule();
        } else if (e.key === 'ArrowRight') {
            daySelect.selectedIndex =
                (index + 1) % daySelect.length;
            updateSchedule();
        }
    });
});
