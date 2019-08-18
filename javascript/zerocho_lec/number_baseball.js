var body = document.body;

var num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var num_array = [];

for (var i = 0; i < 4; i++) {
    var num = num_list.splice(Math.floor(Math.random() * num_list.length), 1)[0];
    num_array.push(num);
}

var result = document.createElement('h1');
body.append(result);
var form = document.createElement('form');
body.append(form);
var input = document.createElement('input');
input.type = 'text';
input.maxLength = 4;
form.append(input);
var button = document.createElement('button');
button.textContent = '입력';
form.append(button);

var failed = 0;
form.addEventListener('submit', function callback(e) {
    //console.dir(e);
    e.preventDefault();
    var answer = input.value;
    console.log(num_array);
    if (answer === num_array.join('')) { // 맞았을 때
        result.textContent = '홈런';
        input.value = '';
        input.focus();

        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
        num_array = [];
        for (var i = 0; i < 4; i++) {
            var num = num_list.splice(Math.floor(Math.random() * num_list.length), 1)[0];
            num_array.push(num);
        }
        failed = 0;
    } else { // 틀렸을 때
        var answer_array = answer.split('');
        var strike = 0;
        var ball = 0;
        failed += 1;
        if (failed > 10) {
            result.textContent = '10번 넘게 틀려서 실패! 답은 ' + num_array.join('') + ' 였습니다.';
            input.value = '';
            input.focus();
            failed = 0;
        }
        for (var i = 0; i < 4; i++)
        {
            if (Number(answer_array[i]) === num_array[i])
            {
                // 같은 자리인지 확인
                strike++;
            } else if (num_array.indexOf(Number(answer_array[i])) > -1) {
                // 같은 자리는 아니지만 숫자가 겹치는지 확인
                ball++;
            }
        }
        result.textContent = String(strike) + ' 스트라이크, ' + String(ball) + ' 볼';
    }
})