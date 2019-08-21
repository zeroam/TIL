var body = document.body;
var table = document.createElement('table');
var rows = [];

function callback(e) {
    console.log(e.target);
};

for (var i = 0; i < 3; i++) {
    var tr = document.createElement('tr');
    rows.push([]);
    for (var j = 0; j < 3; j++)
    {
        var td = document.createElement('td');
        td.addEventListener('click', callback);
        rows[i].push(td);
        tr.appendChild(td);
    }
    table.appendChild(tr);
}
body.appendChild(table);

console.log(rows);