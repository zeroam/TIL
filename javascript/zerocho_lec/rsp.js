var rsp = {
    rock: { name: '바위', value: '0px' },
    scissor: { name: '가위', value: '-142px'},
    paper: { name: '보', value: '-295px'},
};
var result_dict = {
    win: {
        '가위': '보',
        '바위': '가위',
        '보': '바위',
    },
    lose: {
        '가위': '바위',
        '바위': '보',
        '보': '가위',
    },
    draw: {
        '가위': '가위',
        '바위': '바위',
        '보': '보',
    }
};

var computer_select = rsp.rock;

// 사전형 자료구조를 사용하여 가독성 높임
var interval;
function interval_maker() {
    clearInterval(interval);
    interval = setInterval(function () {
        if (computer_select === rsp.rock) {
            computer_select = rsp.scissor;
        } else if (computer_select === rsp.scissor) {
            computer_select = rsp.paper;
        } else {
            computer_select = rsp.rock;
        }
        document.querySelector('#computer')
            .style.backgroundPosition = computer_select.value + ' 0px';
    }, 100);
}
interval_maker();

document.querySelectorAll('.btn').forEach(function (btn) {
    btn.addEventListener('click', function(e) {
        clearInterval(interval);
        setTimeout(function () {
            interval_maker()
        }, 1000);
        var my_select = this.textContent;
        console.log(my_select, computer_select.name);
        if (result_dict.win[my_select] == computer_select.name) {
            console.log('이겼습니다.');
        } else if (result_dict.lose[my_select] == computer_select.name) {
            console.log('졌습니다');
        } else {
            console.log('비겼습니다.');
        }
    });
});