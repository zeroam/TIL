var tbody = document.querySelector('#table tbody')

document.querySelector('#exec').addEventListener('click', function() {
    // 지뢰 테이블 초기화
    tbody.innerHTML = '';

    var hor = parseInt(document.querySelector('#hor').value);
    var ver = parseInt(document.querySelector('#ver').value);
    var mine = parseInt(document.querySelector('#mine').value);
    console.log(hor, ver, mine);
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

    var dataset = []
    for (var i = 0; i < ver; i++) {
        var arr = [];
        var tr = document.createElement('tr');
        for (var j = 0; j < hor; j++) {
            var td = document.createElement('td');
            td.addEventListener('contextmenu', function (e) {
                e.preventDefault();
                e.currentTarget.textContent = '!';
                var par_tr = e.currentTarget.parentNode;
                var par_tbody = par_tr.parentNode;
                // e.target 대신에 td를 사용하게 된다면 클로저 문제가 발생
                var cur_col = Array.prototype.indexOf.call(par_tr.children, e.currentTarget);
                var cur_row = Array.prototype.indexOf.call(par_tbody.children, par_tr);
                dataset[cur_row][cur_col] = '!';
                console.log(dataset);
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

tbody.addEventListener('contextmenu', function (e) {
    console.log(e.currentTarget);
    console.log(e.target);
})