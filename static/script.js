let timetable = {};

function getTypeIcon(type) {
    const icons = {
        'Lecture': '📖',
        'Tutorial': '✏️',
        'Lab': '🔬'
    };
    return icons[type] || '📚';
}

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
                <p><span>${getTypeIcon(cls.type)}</span> ${cls.type} | 📍 ${cls.location}</p>
            </div>
        </div>
    `).join('');
}

function toggleTheme() {
    const html = document.documentElement;
    const button = document.querySelector('.theme-toggle');
    const isDark = html.getAttribute('data-theme') === 'dark';
    html.setAttribute('data-theme', isDark ? 'light' : 'dark');
    button.textContent = isDark ? '🌙 Dark Mode' : '☀️ Light Mode';
}

document.addEventListener('DOMContentLoaded', async () => {
    const daySelect = document.getElementById('daySelect');
    const container = document.getElementById('schedule-container');

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
        container.innerHTML = '<p class="error">Failed to load timetable. Try refreshing.</p>';
    }

    daySelect.addEventListener('change', updateSchedule);

    document.addEventListener('keydown', e => {
        if (e.target === daySelect) return;

        const index = daySelect.selectedIndex;
        if (e.key === 'ArrowLeft') {
            daySelect.selectedIndex = (index - 1 + daySelect.length) % daySelect.length;
            updateSchedule();
        } else if (e.key === 'ArrowRight') {
            daySelect.selectedIndex = (index + 1) % daySelect.length;
            updateSchedule();
        }
    });
});
