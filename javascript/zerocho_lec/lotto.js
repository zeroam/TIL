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