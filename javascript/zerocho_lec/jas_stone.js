var rival = {
    id: 'rival-deck',
    hero_name: 'rival-hero',
    field_name: 'rival-cards',
    deck: document.getElementById('rival-deck'),
    hero: document.getElementById('rival-hero'),
    field: document.getElementById('rival-cards'),
    cost: document.getElementById('rival-cost'),
    deck_data: [],
    hero_data: [],
    field_data: [],
    selected: null,
}

var my = {
    id: 'my-deck',
    hero_name: 'my-hero',
    field_name: 'my-cards',
    deck: document.getElementById('my-deck'),
    hero: document.getElementById('my-hero'),
    field: document.getElementById('my-cards'),
    cost: document.getElementById('my-cost'),
    deck_data: [],
    hero_data: [],
    field_data: [],
    selected: null,
}

var turn = true;
var turn_btn = document.getElementById('turn-btn');

function deck_to_field(turn, target, data)
{
    var who = turn ? my : rival;
    var other = turn ? rival : my;
    var id = target.parentNode.id;

    // 내 덱에 있으면
    if (id == who.id) {
        var cur_cost = Number(who.cost.textContent);
        if (cur_cost < data.cost) {
            return;
        }
        var idx = who.deck_data.indexOf(data);
        who.deck_data.splice(idx, 1);
        who.field_data.push(data);
        who.deck.innerHTML = '';
        who.field.innerHTML = '';
        deck_create(1, who.deck_data, who.deck);
        who.field_data.forEach(function (data) {
            add_card(data, who.field);
        });
        who.cost.textContent = cur_cost - data.cost;

        return;
    }
    // 내 필드에 있으면
    else if(id == who.field_name || id == who.hero_name) {
        // 턴이 끝난 카드면
        if (target.classList.contains('card-turnover')) {
            return;
        }

        // 선택된 카드가 있으면
        if (who.selected) {
            who.selected.classList.remove('card-selected');
            // 선택된 카드가 동일한 카드일 때
            if (who.selected == target)
            {
                who.selected = null;
                who.selected_data = null;
                return;
            }
        }

        who.selected = target;
        who.selected_data = data;
        who.selected.classList.add('card-selected');

        return;
    }
    // 상대 카드면
    else if(id == other.field_name || id == other.hero_name) {
        // 내 카드가 선택되어 있지 않다면
        if (!who.selected) {
            return;
        }

        data.hp = data.hp - who.selected_data.att;
        var card_hp = [].filter.call(target.children, element => element.className == 'card-hp')[0];
        card_hp.textContent = data.hp;
        // 카드가 죽었을 때
        if (data.hp <= 0) {
            // 데이터 제거
            var index = other.field_data.indexOf(data);
            if (index > -1) { // 쫄병이 죽었을 때
                other.field_data.splice(index, 1);
                // 화면 제거
                target.parentNode.removeChild(target);
            }
            else { // 영웅이 죽었을 때
                if (turn) {
                    alert('승리하셨습니다!');
                } else {
                    alert('패배했습니다 ㅜㅜ');
                }
                initilize();
                return;
            }
        }
        who.selected.classList.remove('card-selected');
        who.selected.classList.add('card-turnover');
        who.selected = null;
        who.selected_data = null;
    }
}

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
        var target = e.currentTarget
        deck_to_field(turn, target, data);
    })
    dom.appendChild(card);
}

function deck_create(num, deck_data, deck) {
    for (var i = 0; i < num; i++) {
        deck_data.push(card_factory());
    }

    deck_data.forEach(function (data) {
        add_card(data, deck);
    });
}

function hero_create(hero, hero_data)
{
    hero_data = card_factory(true);
    add_card(hero_data, hero, true);
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

function reset(who) {
    who.field.innerHTML = '';
    who.hero.innerHTML = '';
    who.deck.innerHTML = '';
    who.deck_data = [];
    who.hero_data = [];
    who.field_data = [];
    who.selected = null;
    who.selected_data = null;
    who.cost.textContent = 10;
    deck_create(5, who.deck_data, who.deck);
    hero_create(who.hero, who.hero_data);
}

function initialize() {
    reset(my);
    reset(rival);
}

turn_btn.addEventListener('click', function() {
    turn = !turn;
    var who = turn ? my : rival;

    // 덱 초기화
    who.cost.textContent = 10;
    who.hero.children[0].classList.remove('card-selected');
    who.hero.children[0].classList.remove('card-turnover');
    [].forEach.call(who.field.children, element => {
        element.classList.remove('card-selected');
        element.classList.remove('card-turnover');
    });
    who.selected = null;
    who.selected_data = null;

    document.getElementById('rival').classList.toggle('turn');
    document.getElementById('my').classList.toggle('turn');
});

initialize();