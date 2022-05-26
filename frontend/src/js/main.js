(function () {
  // APIのベースURL
  const API_BASE = "/api";
  // クエリセレクタのエイリアス
  const qs = (selector) => document.querySelector(selector);
  // API一覧
  const API = {
    LOAD: `${API_BASE}/load`,
    MARIAGE: `${API_BASE}/mariage`,
  };
  // BOTUIオブジェクト
  const BOTUI = new BotUI("botui-app");

  function otsumami() {
    BOTUI.message.add({
      delay: 400,
      content: "どのおつまみについて知りたい？",
    });
    return BOTUI.action.text({
      delay: 500,
      action: {
        placeholder: "おつまみ名を入力してください...",
      },
    })
    .then(function (res) { // will be called when it is submitted.
      BOTUI.message.add({
        loading: true,
      }).then(function (index) {
        fetch(`${API.MARIAGE}?q=${res.value}`)
        .then((res) => res.json())
        .then((data) => {
          BOTUI.message.update(index, {
            loading: false,
            content: data.result,
          });  
        }).then(otsumami);
      });
    });
  }

  window.onload = () => {
    qs("#close-chat").addEventListener("click", () => {
      qs("#bot-chat").style.opacity = 0;
    });
    qs("#start-chat").addEventListener("click", () => {
      qs("#bot-chat").style.opacity = 1;
      BOTUI.message.removeAll();
      BOTUI.action.hide();

      BOTUI.message
        .bot({
          content: "日本酒は好きですか?",
        })
        .then(function () {
          return BOTUI.message.add({
            delay: 300,
            content: "合うおつまみと一緒に飲むと、さらに日本酒を楽しめます。",
          });
        })
        .then(function () {
          return BOTUI.message.add({
            delay: 300,
            content: "事前学習済みモデルをロード開始\nしばらくお待ちください。",
          });
        })
        .then(function () {
          BOTUI.message.add({
            loading: true,
          }).then(function (index) {
            // do some stuff like ajax, etc.
            fetch(`${API.LOAD}`)
            .then(function () {
              BOTUI.message.update(index, {
                loading: false,
                content: "事前学習済みモデルをロード完了",
              });  
            }).then(otsumami);
          });
        });
    });
  };
})();
