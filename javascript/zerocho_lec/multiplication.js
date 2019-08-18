var num1 = Math.ceil(Math.random() * 9);
var num2 = Math.ceil(Math.random() * 9);
var result = num1 * num2;

var body = document.body;
var word = document.createElement('div');
word.textContent = String(num1) + ' 곱하기 ' + String(num2) + ' 는? ';
document.body.append(word);

var form = document.createElement('form');
document.body.append(form);
var input = document.createElement('input');
input.type = 'number';
form.append(input);
var button = document.createElement('button');
button.textContent = '입력';
form.append(button);
var result_tag = document.createElement('div');
document.body.append(result_tag);

form.addEventListener('submit', function callback(e) {
    e.preventDefault();
    if (result === Number(input.value)) {
        result_tag.textContent = '딩동댕';
        num1 = Math.ceil(Math.random() * 9);
        num2 = Math.ceil(Math.random() * 9);
        result = num1 * num2;
        word.textContent = String(num1) + ' 곱하기 ' + String(num2) + ' 는? ';
        input.value = '';
        input.focus();
    } else {
        result_tag.textContent = '땡';
        input.value = '';
        input.focus();
    }

});