var screen = document.querySelector('#screen');

var start_time;
var end_time;

screen.addEventListener('click', function (e) {
    if (screen.classList.contains('waiting')) { // 현재 준비 상태인지 파악
        screen.classList.remove('waiting');
        screen.classList.add('ready');
        screen.textContent = '초록색이 되면 클릭하세요';
        setTimeout(function () {
            screen.click();
        }, 1000 * Math.random() + 2000)
    } else if (screen.classList.contains('ready')) {
        screen.classList.remove('ready');
        screen.classList.add('now');
        screen.textContent = '클릭하세요!';
        start_time = new Date();
    } else if (screen.classList.contains('now')) {
        screen.classList.remove('now');
        screen.classList.add('waiting');
        screen.textContent = '클릭해서 시작하세요';
        end_time = new Date();
        console.log('반응속도:', end_time - start_time, 'ms');
    }
});
