'use strict';
window.GAME_DATA = (() => {
 const hero = (id, word, gender, alt) => ({id,word,gender,image:`assets/heroes/hero-${id}.png`,alt});
 const action = (id,word,alt) => ({id,word,image:`assets/actions/action-${id}.png`,alt});
 const object = (id,nominative,accusative,alt) => ({id,nominative,accusative,image:`assets/objects/object-${id}.png`,alt});
 const mood = (id,masculine,feminine,alt) => ({id,masculine,feminine,image:`assets/moods/mood-${id}.png`,alt});
 return {
 heroes:[hero('pavel','Павел','masculine','Павел в голубой футболке'),hero('mila','Мила','feminine','Мила с двумя хвостиками в коралловом платье'),hero('wolf','волк','masculine','Добрый серый волк в бирюзовом комбинезоне'),hero('elephant','слон','masculine','Серый слон в жёлтой футболке'),hero('horse','лошадь','feminine','Коричневая лошадь в зелёном комбинезоне')],
 actions:[action('stroke','гладит','Ладонь гладит спинку белки'),action('break','ломает','Две руки разламывают плитку'),action('catch','ловит','Раскрытые ладони ловят колобка'),action('push','толкает','Фигура упирается руками в лодку и толкает её'),action('put-to-bed','укладывает','Рука укладывает куклу в кроватку')],
 objects:[object('squirrel','белка','белку','Рыжая белка с пушистым хвостом'),object('chocolate','шоколад','шоколад','Плитка шоколада без упаковки'),object('kolobok','колобок','колобка','Золотистый сказочный колобок'),object('boat','лодка','лодку','Деревянная лодка'),object('doll','кукла','куклу','Кукла в сиреневом платье с игрушечными суставами')],
 moods:[mood('happy','весёлый','весёлая','Весёлое жёлтое личико'),mood('sad','грустный','грустная','Грустное жёлтое личико'),mood('surprised','удивлённый','удивлённая','Удивлённое жёлтое личико'),mood('angry','сердитый','сердитая','Сердитое жёлтое личико'),mood('sleepy','сонный','сонная','Сонное жёлтое личико')],
 pairs:[{id:'stroke_squirrel',actionId:'stroke',objectId:'squirrel'},{id:'break_chocolate',actionId:'break',objectId:'chocolate'},{id:'catch_kolobok',actionId:'catch',objectId:'kolobok'},{id:'push_boat',actionId:'push',objectId:'boat'},{id:'put_doll_to_bed',actionId:'put-to-bed',objectId:'doll'}],
 backgrounds:['assets/backgrounds/game-background.png','assets/backgrounds/cover-background.png']};
})();
