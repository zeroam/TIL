var lotto_nums = Array(45)
    .fill()
    .map(function(item, index) {
    return index + 1;
});
console.log(lotto_nums);

var shuffle = [];
while (lotto_nums.length > 0) {
    var value = lotto_nums.splice(Math.floor(Math.random() * lotto_nums.length), 1)[0];
    shuffle.push(value);
}
console.log(shuffle);
var bonus = shuffle[shuffle.length - 1];
var nums = shuffle.slice(0, 6);
console.log('당첨숫자들', nums.sort(function (p, c) { return p - c; }), '보너스', bonus);

var result_tag = document.getElementById('result');

function create_ball(tag, number) {
    var ball = document.createElement('div');
    ball.textContent = number;
    ball.style.display = 'inline-block';
    ball.style.border = '1px solid black';
    // css와 다른점
    ball.style.borderRadius = '10px';
    ball.style.width = '20px';
    ball.style.height = '20px';
    ball.style.textAlign = 'center';
    ball.style.verticalAlign = 'center';
    ball.style.marginRight = '10px';
    ball.style.fontSize = '15px';
    var color;
    if (number <= 10) {
        color = 'red';
    } else if (number <= 20) {
        color = 'orange';
    } else if (number <= 30) {
        color = 'yellow';
    } else if (number <= 40) {
        color = 'blue';
    } else {
        color = 'green';
    }
    ball.style.backgroundColor = color;
    tag.appendChild(ball);
}

// 클로저 문제
for (let i = 0; i < nums.length; i++) {
    setTimeout(function callback() {
        create_ball(result_tag, nums[i]);
    }, 1000 * (i + 1));
}

setTimeout(function callback() {
    var bonus_tag = document.getElementsByClassName('bonus')[0];
    create_ball(bonus_tag, bonus);
}, 7000);
