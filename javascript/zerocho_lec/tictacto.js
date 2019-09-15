var body = document.body;
var table = document.createElement('table');
var tds = [];
var trs = [];
var blanks = [];
var turn = 'X';
var flag = false;
var result = document.createElement('div');

function is_win(tr_index, td_index) {
    // 세칸 다 채워졌나?
    var filled = false;
    // 가로줄 검사
    if (tds[tr_index][0].textContent  === turn && 
        tds[tr_index][1].textContent  === turn &&
        tds[tr_index][2].textContent  === turn) {
        filled = true;
    }
    // 세로줄 검사
    if (tds[0][td_index].textContent  === turn &&
        tds[1][td_index].textContent  === turn &&
        tds[2][td_index].textContent  === turn) {
        filled = true;
    }
    // 대각선 검사
    if (tds[0][0].textContent === turn &&
        tds[1][1].textContent === turn &&
        tds[2][2].textContent  === turn) {
        filled = true;
    }
    if (tds[2][0].textContent === turn &&
        tds[1][1].textContent === turn &&
        tds[0][2].textContent  === turn) {
        filled = true;
    }

    return filled;
}

function initialize() {
    turn = turn === 'X' ? 'O' : 'X';
    blanks = [];
    tds.forEach(function (row) {
        row.forEach(function (col) {
            col.textContent = '';
            blanks.push(col);
        });
    });
    
    // 컴퓨터 턴이면
    if (turn === 'O') {
        setTimeout(function () {
            blanks[Math.floor(Math.random() * blanks.length)].click();
        }, 1000);
    }
}

function callback(e) {
    // 컴퓨터 클릭 도중일 때,
    if (flag) {
        return;
    }
    var tr_index = trs.indexOf(e.target.parentNode);
    var td_index = tds[tr_index].indexOf(e.target);

    if (tds[tr_index][td_index].textContent !== '') { // 칸이 이미 채워져 있는가?
        console.log('빈칸 아닙니다.');
    } else { // 빈칸이면
        console.log('빈칸 입니다.');
        tds[tr_index][td_index].textContent = turn;

        var win = is_win(tr_index, td_index);
        // 빈칸 재설정
        blanks = blanks.filter(function (td) { return td.textContent === ''; })

        // 승리시
        if (win) {
            result.textContent = turn + ' 승리';
            initialize();
        } else if (blanks.length === 0) { // 무승부시
            result.textContent = '무승부';
            initialize();
        } else {    // 다 안찼으면
            if (turn === 'X') { 
                turn = 'O';
                console.log('컴퓨터의 턴입니다.');
                // 빈 칸 중 하나를 고른다
                flag = true;
                setTimeout(function () {
                    flag = false;
                    blanks[Math.floor(Math.random() * blanks.length)].click();
                }, 1000);
            } else if (turn === 'O') {
                console.log('사용자의 턴입니다.');
                turn = 'X';
            }
        }
    }
};

for (var i = 0; i < 3; i++) {
    var tr = document.createElement('tr');
    trs.push(tr);
    tds.push([]);
    for (var j = 0; j < 3; j++)
    {
        var td = document.createElement('td');
        td.addEventListener('click', callback);
        tds[i].push(td);
        tr.appendChild(td);

        blanks.push(td);
    }
    table.appendChild(tr);
}
body.appendChild(table);
body.appendChild(result);

console.log(trs);
console.log(tds);
