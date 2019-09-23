var width = 4;
var height = 3;
var colors_list = ['red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow',
            'white', 'white', 'pink', 'pink'];
var colors = [];
var click_flag = true;
var click_card = [];
var complete_cards = [];
var start_time;

function shuffle() {
    colors = [];
    var list = colors_list.slice();
    // for(var i = 0; colors_list.length > 0; i++) {
    while (list.length > 0) {
        colors = colors.concat(list.splice(Math.floor(Math.random() * list.length), 1))
    }

    console.log(colors);
}

function card_setting(width, height) {
    // 초기화
    document.querySelector('#wrapper').innerHTML = '';
    complete_cards = [];
    shuffle(colors_list);

    var cardWrapper = document.createElement('div');
    for (var i = 0; i < width * height + 1; i++) {
        click_flag = false;
        var card = document.createElement('div');
        //card.classList.add('card');
        card.className = 'card';    // 하나만 추가하는 경우
        var cardInner = document.createElement('div');
        cardInner.className = 'card-inner';
        var cardFront = document.createElement('div');
        cardFront.className = 'card-front';
        var cardBack = document.createElement('div');
        cardBack.className = 'card-back';
        cardBack.style.backgroundColor = colors[i];
        cardInner.appendChild(cardFront);
        cardInner.appendChild(cardBack);
        card.appendChild(cardInner);
        // card.addEventListener('click', function () {
        //     card.classList.toggle('flipped');
        // });
        (function (card) {
            card.addEventListener('click', function (e) {
                if (!click_flag || complete_cards.includes(card)) {
                    return;
                }
                card.classList.toggle('flipped');
                click_card.push(e.currentTarget);
                if (click_card.length === 2) {
                    // 같은 카드를 두 번 클릭하면
                    if (click_card[0].querySelector('.card-back') === click_card[1].querySelector('.card-back')) {
                        click_card = [];
                    } else if ( // 두 카드의 색깔이 같으면
                        click_card[0].querySelector('.card-back').style.backgroundColor === 
                        click_card[1].querySelector('.card-back').style.backgroundColor) {
                        complete_cards.push(click_card[0]);
                        complete_cards.push(click_card[1]);
                        click_card = [];
                        if (complete_cards.length === width * height) {
                            var time = new Date() - start_time;
                            alert('축하합니다. 성공!, ' + time / 1000 + '초 걸렸습니다.');
                            card_setting(width, height);
                        }
                    } else { // 두 카드의 색깔이 다르면
                        click_flag = false;
                        setTimeout(function() {
                            click_card.forEach(function (card) {
                                card.classList.remove('flipped');
                                card.click();
                            });
                            click_flag = true;
                            click_card = [];
                        }, 1000);
                    }
                }
            });
        })(card);
        cardWrapper.appendChild(card);
    }
    // 동적으로 width 생성
    document.body.appendChild(card);
    var style = getComputedStyle(card);
    cardWrapper.style.width = (parseInt(style.width) + parseInt(style.marginRight) + 5) * width + "px";
    document.body.removeChild(card);
    document.querySelector('#wrapper').appendChild(cardWrapper);

    document.querySelectorAll('.card').forEach(function (card, index) {
        setTimeout(function() {
            card.classList.add('flipped');
        }, 1000 + 100 * index);
    });

    setTimeout(function() {
        document.querySelectorAll('.card').forEach(function (card, index) {
            card.classList.remove('flipped');
        });
        click_flag = true;
        start_time = new Date();
    }, 5000);
}

card_setting(width, height);