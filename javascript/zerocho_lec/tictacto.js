var body = document.body;
var table = document.createElement('table');
var tds = [];
var trs = [];
var turn = 'X';
var result = document.createElement('div');

function callback(e) {
    var tr_index = trs.indexOf(e.target.parentNode);
    console.log('몇줄', tr_index);
    var td_index = tds[tr_index].indexOf(e.target);
    console.log('몇칸', td_index);

    if (tds[tr_index][td_index].textContent !== '') { // 칸이 이미 채워져 있는가?
        console.log('빈칸 아닙니다.');
    } else { // 빈칸이면
        console.log('빈칸 입니다.');
        tds[tr_index][td_index].textContent = turn;
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
        if (tr_index === td_index) {
            if (tds[0][0].textContent === turn &&
                tds[1][1].textContent === turn &&
                tds[2][2].textContent  === turn) {
                filled = true;
            }
        }
        if (Math.abs(tr_index - td_index) === 2) {
            if (tds[2][0].textContent === turn &&
                tds[1][1].textContent === turn &&
                tds[2][0].textContent  === turn) {
                filled = true;
            }
        }

        if (filled) {
            console.log(turn + ' 승리!');
            result.textContent = turn + ' 승리';
            // 초기화
            turn = 'X';
            tds.forEach(function (row) {
                row.forEach(function (col) {
                    col.textContent = '';
                })
            })
        } else {
            turn = turn === 'X' ? 'O' : 'X';
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
    }
    table.appendChild(tr);
}
body.appendChild(table);
body.appendChild(result);

console.log(trs);
console.log(tds);
