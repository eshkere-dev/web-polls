const polls = []; // Массив для хранения опросов
// Функция для отображения опросов
function renderPolls() {
    const container = document.getElementById('pollsContainer');
    container.innerHTML = ''; // Очищаем контейнер
    // Проверяем, есть ли опросы
    if (polls.length === 0) {
        container.innerHTML = '<p>Нет доступных опросов.</p>';
        return;
    }
    // Отображаем каждый опрос
    polls.forEach((poll, index) => {
        const pollDiv = document.createElement('div');
        pollDiv.innerHTML = `
            <h3>${poll.title}</h3>
            <button onclick="editPoll(${index})">Редактировать</button>
            <button onclick="deletePoll(${index})">Удалить</button>
        `;
        container.appendChild(pollDiv);
    });
}
// Функция для добавления нового опроса
function addPoll() {
    const title = prompt("Введите название опроса:");
    if (title) {
        polls.push({ title, questions: [] });
        renderPolls();
    }
}
// Функция для редактирования опроса
function editPoll(index) {
window.location.href = `editPoll.html?index={index}`;

}
// Функция для удаления опроса
function deletePoll(index) {
    if (confirm("Вы уверены, что хотите удалить этот опрос?")) {
        polls.splice(index, 1); // Удаляем опрос по индексу
        renderPolls(); // Обновляем отображение опросов
    }
}
// Привязываем обработчик события к кнопке добавления опроса
document.getElementById('addPollButton').addEventListener('click', addPoll);
// Инициализируем отображение опросов при загрузке страницы
renderPolls();