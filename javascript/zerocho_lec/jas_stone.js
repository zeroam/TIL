var rival_deck = document.getElementById('rival-deck');
var rival_hero = document.getElementById('rival-hero');
var rival_field = document.getElementById('rival-cards');
var rival_cost = document.getElementById('rival-cost');
var rival_deck_data = [];
var rival_hero_data = [];
var rival_field_data = [];

var my_deck = document.getElementById('my-deck');
var my_hero = document.getElementById('my-hero');
var my_field = document.getElementById('my-cards');
var my_cost = document.getElementById('my-cost');
var my_deck_data = [];
var my_hero_data = [];
var my_field_data = [];

var turn = true;
var turn_btn = document.getElementById('turn-btn');

function add_card(data, dom, is_hero) {
    var card = document.querySelector('.card-hidden .card').cloneNode(true);
    card.querySelector('.card-cost').textContent = data.cost;
    card.querySelector('.card-att').textContent = data.att;
    card.querySelector('.card-hp').textContent = data.hp;

    if (is_hero) {
        card.querySelector('.card-cost').style.display = 'none';
        var name = document.createElement('div');
        name.classList.add('card-name');
        name.textContent = '영웅';
        card.appendChild(name);
    }

    card.addEventListener('click', function (e) {
        if (turn) { // 내턴
            // data는 클로저
            // 내 카드인지 확인
            if (e.currentTarget.parentNode.id !== 'my-deck') {
                return;
            }
            var cur_cost = Number(my_cost.textContent);
            if (cur_cost < data.cost) {
                return;
            }
            var idx = my_deck_data.indexOf(data);
            my_deck_data.splice(idx, 1);
            my_field_data.push(data);
            my_deck.innerHTML = '';
            my_field.innerHTML = '';
            my_deck_create(1);
            my_field_data.forEach(function (data) {
                add_card(data, my_field);
            });
            my_cost.textContent = cur_cost - data.cost;
        } else {    // 상대턴
            if (e.currentTarget.parentNode.id !== 'rival-deck') {
                return;
            }
            var cur_cost = Number(rival_cost.textContent);
            if (cur_cost < data.cost) {
                return;
            }
            var idx = rival_deck_data.indexOf(data);
            rival_deck_data.splice(idx, 1);
            rival_field_data.push(data);
            rival_deck.innerHTML = '';
            rival_field.innerHTML = '';
            rival_deck_create(1);
            rival_field_data.forEach(function (data) {
                add_card(data, rival_field);
            });
            rival_cost.textContent = cur_cost - data.cost;
        }
    })
    dom.appendChild(card);
}

function rival_deck_create(num) {
    for (var i = 0; i < num; i++) {
        rival_deck_data.push(card_factory());
    }

    rival_deck_data.forEach(function (data) {
        add_card(data, rival_deck);
    });
}

function rival_hero_create() {
    rival_hero_data = card_factory(true);
    add_card(rival_hero_data, rival_hero, true);
}

function my_deck_create(num) {
    for (var i = 0; i < num; i++) {
        my_deck_data.push(card_factory());
    }

    my_deck_data.forEach(function (data) {
        add_card(data, my_deck);
    });
}

function my_hero_create() {
    my_hero_data = card_factory(true);
    add_card(my_hero_data, my_hero, true);
}

function Card(is_hero) {
    if (is_hero) {
        this.att = Math.ceil(Math.random() * 5);
        this.hp = Math.ceil(Math.random() * 5) + 25;
    }
    else {
        this.att = Math.ceil(Math.random() * 5);
        this.hp = Math.ceil(Math.random() * 5);
        this.cost = Math.floor((this.att + this.hp) / 2);
    }
}

function card_factory(is_hero) {
    return new Card(is_hero);
}

function initilize() {
    rival_deck_create(5);
    rival_hero_create();
    my_deck_create(5);
    my_hero_create();
}

turn_btn.addEventListener('click', function() {
    turn = !turn;
    if (turn) {
        my_cost.textContent = 10;
    } else {
        rival_cost.textContent = 10;
    }
    document.getElementById('rival').classList.toggle('turn');
    document.getElementById('my').classList.toggle('turn');
});

initilize();