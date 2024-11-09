// index_script.js
let isRussian = true; // Переменная для отслеживания текущего языка
// Обработчик события для кнопки переключения языка
document.getElementById('language-button').addEventListener('click', function() {
isRussian = !isRussian; // Переключаем язык
updateLanguage(); // Обновляем текст на странице
});
// Функция для обновления текста на странице
function updateLanguage() {
if (isRussian) {
document.querySelector('h1').innerText = 'Конструктор опросов';
document.querySelector('.cta').innerText = 'Создать опрос';
document.querySelector('#intro h2').innerText = 'Эффективное решение для рекрутеров';
document.querySelector('#intro p').innerText = 'Создавайте и управляйте опросами с легкостью. Наш конструктор предлагает интуитивно понятный интерфейс и мощные инструменты для анализа данных.';
document.querySelector('#features h2').innerText = 'Функциональные возможности';
document.querySelector('#features ul').innerHTML = `
<li>Создание различных типов вопросов: текстовые, множественный выбор, шкалы и т.д.</li>
<li>Интуитивно понятный интерфейс для настройки и редактирования опросов.</li>
<li>Инструменты для анализа и визуализации результатов опросов.</li>
<li>Интеграция с существующими HR-системами.</li>
<li>Адаптивный дизайн для всех устройств.</li>
`;

document.querySelector('#examples h2').innerText = 'Примеры использования';
document.querySelector('#examples p').innerText = 'Наш конструктор подходит для:';
document.querySelector('#examples ul').innerHTML = `
<li>Оценки кандидатов на собеседованиях.</li>
<li>Сбора обратной связи от сотрудников.</li>
<li>Проведения исследований и опросов.</li>
`;

document.querySelector('footer p').innerText = '© 2024 Конструктор Опросов.';
} else {
document.querySelector('h1').innerText = 'Survey builder';
document.querySelector('.cta').innerText = 'Create survey';
document.querySelector('#intro h2').innerText = 'Effective Solution for Recruiters';
document.querySelector('#intro p').innerText = 'Create and manage surveys with ease. Our builder offers an intuitive interface and powerful tools for data analysis.';
document.querySelector('#features h2').innerText = 'Features';
document.querySelector('#features ul').innerHTML = `
<li>Creation of various question types: text, multiple choice, scales, etc.</li>
<li>Intuitive interface for setting up and editing surveys.</li>
<li>Tools for analyzing and visualizing survey results.</li>
<li>Integration with existing HR systems.</li>
<li>Responsive design for all devices.</li>
`;
document.querySelector('#examples h2').innerText = 'Usage Examples';
document.querySelector('#examples p').innerText = 'Our builder is suitable for:';
document.querySelector('#examples ul').innerHTML = `
<li>Evaluating candidates in interviews.</li>
<li>Collecting feedback from employees.</li>
<li>Conducting research and surveys.</li>
`;
document.querySelector('footer p').innerText = '© 2024 Survey Builder.';
}
}
// Инициализация языка при загрузке страницы
updateLanguage();

document.getElementById("createsurvey").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default behavior (e.g., page reload)

        // Optionally, show a loading spinner or alert user that something is happening

        // Send AJAX request to Flask server to create the survey
        fetch('/createsurvey', {
            method: 'POST',  // Using POST method (or GET if appropriate)
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                // You can send data to Flask in this JSON object
                action: 'create_survey'
            })
        })
        .then(response => response.json()) // Parse the JSON response from Flask
        .then(data => {
            // Handle the response from Flask here
            if (data.status === 'success') {
                alert("Survey created successfully!");
                // You can also update the page, redirect, or show a modal based on the response
            } else {
                alert("Error creating survey.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });