
let isEnglish = false; // Переменная для отслеживания текущего языка
document.getElementById('translate-button').addEventListener('click', function() {
isEnglish = !isEnglish; // Переключаем язык
if (isEnglish) {
// Перевод текста на английский
document.getElementById('registration-title').innerText = 'Registration';

document.querySelector('input[placeholder="Имя пользователя"]').placeholder = 'Username';
document.querySelector('input[placeholder="Пароль"]').placeholder = 'Password';
document.querySelector('input[placeholder="Электронная почта"]').placeholder = 'Email';
document.querySelector('input[placeholder="Повторите пароль"]').placeholder = 'Repeat Password';
document.querySelector('button[type="submit"]').innerText = 'Register'; // Кнопка "Зарегистрироваться"
document.querySelector('button[type="submitt"]').innerText = 'Sign in';

document.getElementById('login-title').innerText = 'Login';
document.querySelector('input[placeholder="Электронная почта"]').placeholder = 'Email';
document.querySelector('input[placeholder="Пароль"]').placeholder = 'Password';

} else {
// Перевод текста на русский
document.getElementById('registration-title').innerText = 'Регистрация';

document.querySelector('input[placeholder="Username"]').placeholder = 'Имя пользователя';
document.querySelector('input[placeholder="Email"]').placeholder = 'Электронная почта';
document.querySelector('input[placeholder="Password"]').placeholder = 'Пароль';
document.querySelector('input[placeholder="Repeat Password"]').placeholder = 'Повторите пароль';
document.querySelector('button[type="submit"]').innerText = 'Зарегистрироваться'; // Кнопка "Зарегистрироваться"
document.querySelector('button[type="submitt"]').innerText = 'Войти';
document.getElementById('login-title').innerText = 'Вход';
document.querySelector('input[placeholder="Email"]').placeholder = 'Электронная почта';
document.querySelector('input[placeholder="Password"]').placeholder = 'Пароль';

}

// Обновляем текст кнопки перевода
document.getElementById('translate-button').innerText = isEnglish ? 'RU' : 'EN';
});