document.getElementById('registration-form').addEventListener('submit', function(event) {
event.preventDefault(); // Предотвращаем стандартное поведение формы
// Получаем значения из полей ввода
const username = document.getElementById('username').value.trim();
const email = document.getElementById('email').value.trim();
const password = document.getElementById('password').value;
const repeatPassword = document.getElementById('repeat-password').value;
// Валидация данных
if (username === '') {
alert('Имя пользователя не может быть пустым.');
return;
}
if (email === '') {
alert('Электронная почта не может быть пустой.');
return;
}
if (password.length < 6) {
alert('Пароль должен содержать не менее 6 символов.');
return;
}
if (password !== repeatPassword) {
alert('Пароли не совпадают.');
return;
}
// Здесь вы можете добавить логику для отправки данных на сервер
console.log('Регистрация успешна:', {
username: username,
email: email,
password: password
});
// Очистка формы после успешной регистрации
document.getElementById('registration-form').reset();
});