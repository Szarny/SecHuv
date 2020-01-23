const FROM = {
    BOT: 1,
    USER: 2
}

const send_button = $("#send-button");
const chat_div = $("#chat-div");
const chat_input = $("#chat-input");
const chat_form = $("#chat-form");

const add_chat = (from, message) => {
    if (from === FROM.BOT) {
        const bot_chat_element = `<article class="message is-danger sechuv-bot"><div class="message-body sechuv-bot-body">${message}</div></article>`;
        chat_div.append(bot_chat_element);
        $("html,body").animate({scrollTop:$($('.message')[$('.message').length-1]).offset().top});
    }
    
    if (from === FROM.USER) {
        const user_chat_element = `<article class="message sechuv-user"><div class="message-body sechuv-user-body">${message}</div></article>`;
        chat_div.append(user_chat_element);
        $("html,body").animate({scrollTop:$($('.message')[$('.message').length-1]).offset().top});
    }
}
const chat_engine = () => {
    add_chat(FROM.BOT, "分かりました。チェックを行うので受信したメッセージ本文を送信してください。");
}

const input_chat = (e) => {
    if(chat_input.val()){
        add_chat(FROM.USER, chat_input.val());
        chat_input.val("");
        chat_engine();
    }
    e.preventDefault();
}

chat_form.on("submit", input_chat);