// Основной JavaScript для fitness-club-django

// Функция для отображения уведомлений
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        background: ${type === 'success' ? '#4caf50' : '#f44336'};
        color: white;
        border-radius: 8px;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
}

// Функция для форматирования даты
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Функция для отображения прогресса клиента (график)
function renderProgressChart(ctx, data) {
    if (typeof Chart !== 'undefined') {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.map(d => d.date),
                datasets: [{
                    label: 'Вес (кг)',
                    data: data.map(d => d.weight),
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    title: { display: true, text: 'Прогресс веса' }
                }
            }
        });
    }
}

// API-клиент для взаимодействия с бэкендом
const api = {
    baseUrl: '/api',
    token: localStorage.getItem('token'),
    
    async request(endpoint, method = 'GET', data = null) {
        const headers = {
            'Content-Type': 'application/json',
        };
        if (this.token) {
            headers['Authorization'] = `Token ${this.token}`;
        }
        
        const config = {
            method,
            headers,
        };
        
        if (data) {
            config.body = JSON.stringify(data);
        }
        
        const response = await fetch(`${this.baseUrl}${endpoint}`, config);
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Ошибка запроса');
        }
        return response.json();
    },
    
    setToken(token) {
        this.token = token;
        if (token) {
            localStorage.setItem('token', token);
        } else {
            localStorage.removeItem('token');
        }
    },
    
    // Пользователи
    login(username, password) {
        return this.request('/users/login/', 'POST', { username, password });
    },
    
    register(data) {
        return this.request('/users/register/', 'POST', data);
    },
    
    getCurrentUser() {
        return this.request('/users/me/');
    },
    
    // Клиенты
    getClients() {
        return this.request('/clients/profiles/');
    },
    
    getClientProfile(id) {
        return this.request(`/clients/profiles/${id}/`);
    },
    
    // Тренировки
    getPrograms() {
        return this.request('/workouts/programs/');
    },
    
    getWorkouts() {
        return this.request('/workouts/workouts/');
    },
    
    addSetResult(workoutExerciseId, data) {
        return this.request(`/workouts/workout-exercises/${workoutExerciseId}/add_set_result/`, 'POST', data);
    },
    
    // Расписание
    getBookings() {
        return this.request('/schedule/bookings/');
    },
    
    createBooking(data) {
        return this.request('/schedule/bookings/', 'POST', data);
    },
    
    // Аналитика
    getTrainerLoad() {
        return this.request('/analytics/trainer_load/');
    },
    
    getClientProgress() {
        return this.request('/analytics/client_progress/');
    }
};

// Экспорт для использования в других файлах
window.api = api;
window.showNotification = showNotification;
window.formatDate = formatDate;
