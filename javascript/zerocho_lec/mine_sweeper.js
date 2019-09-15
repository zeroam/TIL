var tbody = document.querySelector('#table tbody');
var dataset = [];
var stopflag = false;
var opened = 0;

function find_mine_number(dataset, row, col) {
    var arr = [dataset[row][col - 1], dataset[row][col + 1]];
    if (dataset[row - 1]) {
        arr.push(dataset[row - 1][col - 1]);
        arr.push(dataset[row - 1][col]);
        arr.push(dataset[row - 1][col + 1]);
    }
    if (dataset[row + 1]) {
        arr.push(dataset[row + 1][col - 1]);
        arr.push(dataset[row + 1][col]);
        arr.push(dataset[row + 1][col + 1]);
    }
    return arr.filter(function (v) {
            return v === 'X';
        }).length;
}

function click_recursive(row, col) {
    var arr = [tbody.children[row].children[col - 1], tbody.children[row].children[col + 1]];
    if (tbody.children[row - 1]) {
        arr.push(tbody.children[row - 1].children[col - 1]);
        arr.push(tbody.children[row - 1].children[col]);
        arr.push(tbody.children[row - 1].children[col + 1]);
    }
    if (tbody.children[row + 1]) {
        arr.push(tbody.children[row + 1].children[col - 1]);
        arr.push(tbody.children[row + 1].children[col]);
        arr.push(tbody.children[row + 1].children[col + 1]);
    }
    arr.filter(function (v) {
        return !!v;
    }).forEach(function (item) {
        item.click();
    });
}
// function click_recursive(row, col) {
//     var arr = [tbody.children[row].children[col - 1], tbody.children[row].children[col + 1]];
//     if (tbody.children[row - 1]) {
//         arr = arr.concat([tbody.children[row - 1].children[col - 1], 
//             tbody.children[row - 1].children[col],
//             tbody.children[row - 1].children[col + 1]])
//     }
//     if (tbody.children[row + 1]) {
//         arr = arr.concat([tbody.children[row + 1].children[col - 1], 
//             tbody.children[row + 1].children[col],
//             tbody.children[row + 1].children[col + 1]])
//     }
//     // undefined, null 이 아닌 값들만 받음
//     arr.filter(function (v) {
//         return !!v;
//     }).forEach(function (item) {
//         // var par_tr = item.parentNode;
//         // var par_tbody = par_tr.parentNode;
//         // var cur_col = Array.prototype.indexOf.call(par_tr.children, item);
//         // var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
//         // if (dataset[cur_row][cur_col] !== 1) {
//         //     item.click();
//         // }
//         item.click();
//     });
// }

// 콜백함수
function right_callback(e) {
    e.preventDefault();

    if (stopflag === true) {
        return;
    }

    var par_tr = e.currentTarget.parentNode;
    var par_tbody = par_tr.parentNode;
    // e.target 대신에 td를 사용하게 된다면 클로저 문제가 발생
    var cur_col = Array.prototype.indexOf.call(par_tr.children, e.currentTarget);
    var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
    if (['', 'X'].includes(e.currentTarget.textContent)) {
        e.currentTarget.classList.add('flag');
        e.currentTarget.textContent = '!';
    } else if (e.currentTarget.textContent === '!') {
        e.currentTarget.classList.remove('flag');
        e.currentTarget.classList.add('question');
        e.currentTarget.textContent = '?';
    } else {
        e.currentTarget.classList.remove('question');
        if (dataset[cur_row][cur_col] === 0) {
            e.currentTarget.textContent = '';
        } else if (dataset[cur_row][cur_col] === 'X') {
            e.currentTarget.textContent = 'X';
        }
    }
}

document.querySelector('#exec').addEventListener('click', function() {
    // 지뢰 테이블 초기화
    tbody.innerHTML = '';
    // 데이터 셋 초기화
    dataset = []
    // 플래그 초기화
    stopflag = false;
    // 연 칸 초기화
    opened = 0;
    // 결과창 초기화
    document.querySelector('#result').textContent = '';

    var hor = parseInt(document.querySelector('#hor').value);
    var ver = parseInt(document.querySelector('#ver').value);
    var mine = parseInt(document.querySelector('#mine').value);
    var num_list = Array(hor * ver)
        .fill()
        .map(function (item, index) {
            return index;
        });

    // 지뢰 테이블 만들기
    var shuffle = [];
    for (var i = 0; i < mine; i++) {
        var value = num_list.splice(Math.floor(Math.random() * num_list.length), 1)[0];
        shuffle.push(value);
    }

    for (var i = 0; i < ver; i++) {
        var arr = [];
        var tr = document.createElement('tr');
        for (var j = 0; j < hor; j++) {
            var td = document.createElement('td');
            td.addEventListener('contextmenu', right_callback);
            td.addEventListener('click', function callback(e) {
                // 게임 종료
                if (stopflag === true) {
                    return;
                }

                // 표시 해놓은 문자 클릭 방지
                if (['?', '!'].includes(e.currentTarget.textContent)) {
                    return;
                }

                // 클릭 이벤트 핸들러 제거
                e.currentTarget.removeEventListener('click', callback, false);
                e.currentTarget.removeEventListener('contextmenu', right_callback, false);
                e.currentTarget.addEventListener('contextmenu', function (e) {
                    console.dir(e);
                    e.preventDefault();
                })

                var par_tr = e.currentTarget.parentNode;
                var par_tbody = par_tr.parentNode;
                var cur_col = Array.prototype.indexOf.call(par_tr.children, e.currentTarget);
                var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
                e.currentTarget.classList.add('opened');
                if (dataset[cur_row][cur_col] === 'X') {
                    e.currentTarget.textContent = '펑';
                    document.querySelector('#result').textContent = '실패';
                    stopflag = true;
                } else {
                    // 클릭 플래그 활성화 -> 재귀 호출 반복 막기 위해
                    dataset[cur_row][cur_col] = 1;
                    var mine_number = find_mine_number(dataset, cur_row, cur_col);
                    if (mine_number === 0) {
                        // 주변 8칸 동시 오픈(재귀 함수)
                        click_recursive(cur_row, cur_col);
                    }
                    e.currentTarget.textContent = mine_number || '';
                }

                opened += 1;
                // 모두 열었으면
                if (opened == hor * ver - mine) {
                    stopflag = true;
                    document.querySelector('#result').textContent = '승리';
                }
            });
            tr.append(td);
            arr.push(0);
        }
        tbody.append(tr);
        dataset.push(arr);
    }
    // 지뢰 심기
    for (var i = 0; i < mine; i++) {
        var row = Math.floor(shuffle[i] / hor);
        var col = shuffle[i] % hor;
        tbody.children[row].children[col].textContent = 'X';
        dataset[row][col] = 'X';
    }

    console.log(dataset);
});
