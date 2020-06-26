var domain = 'https://skiog.ru/'

window.onload = function() {
  var notif = document.getElementById('notif'),
      spannot = document.getElementById('spannot'),
      not1 = document.getElementById('not1'),
      not2 = document.getElementById('not2'),
      zapros = new XMLHttpRequest();
  zapros.onreadystatechange = function() {
    if (zapros.readyState == 4){
      if (zapros.status == 200){
        var data = JSON.parse(zapros.responseText);
        notif.innerHTML = data['kolvosogl'] + data['kollno'];
        spannot.innerHTML = data['kolvosogl'] + data['kollno'] + ' Уведомлений';
        not1.innerHTML = '<i class="fas fa-envelope mr-2"></i>' + data['kollno'] + ' нераспределенных жалоб';
        not2.innerHTML = '<i class="fas fa-envelope mr-2"></i>' + data['kolvosogl'] + ' ответов на согласовании';
      }
    }
  };

  function answerLoad() {
    zapros.open('GET', domain + 'api/answer/', true);
    zapros.send();
  }

  answerLoad();
};


