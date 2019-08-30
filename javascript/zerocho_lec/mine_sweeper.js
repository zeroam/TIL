var tbody = document.querySelector('#table tbody')

function create_number(dataset, row, col) {
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

document.querySelector('#exec').addEventListener('click', function() {
    // 지뢰 테이블 초기화
    tbody.innerHTML = '';

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

    // 데이터 셋 초기화
    var dataset = []
    for (var i = 0; i < ver; i++) {
        var arr = [];
        var tr = document.createElement('tr');
        for (var j = 0; j < hor; j++) {
            var td = document.createElement('td');
            td.addEventListener('contextmenu', function (e) {
                e.preventDefault();
                var par_tr = e.currentTarget.parentNode;
                var par_tbody = par_tr.parentNode;
                // e.target 대신에 td를 사용하게 된다면 클로저 문제가 발생
                var cur_col = Array.prototype.indexOf.call(par_tr.children, e.currentTarget);
                var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
                if (['', 'X'].includes(e.currentTarget.textContent)) {
                    e.currentTarget.textContent = '!';
                } else if (e.currentTarget.textContent === '!') {
                    e.currentTarget.textContent = '?';
                } else {
                    if (dataset[cur_row][cur_col] === 1) {
                        e.currentTarget.textContent = '';
                    } else {
                        e.currentTarget.textContent = 'X';
                    }
                }
                console.log(dataset);
            });
            td.addEventListener('click', function (e) {
                var par_tr = e.currentTarget.parentNode;
                var par_tbody = par_tr.parentNode;
                var cur_col = Array.prototype.indexOf.call(par_tr.children, e.currentTarget);
                var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
                if (dataset[cur_row][cur_col] === 'X') {
                    e.currentTarget.textContent = '펑';
                } else {
                    e.currentTarget.textContent = create_number(dataset, cur_row, cur_col);
                }
            });
            tr.append(td);
            arr.push(1);
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

var x = 'global';

function ex() {
    var x = 'local';
    console.log(x);
    function call() {
        x = 'change';
    }
    console.dir(call);
    call();
    console.log(x);
}

ex();
console.log(x);
//window.alert(x);