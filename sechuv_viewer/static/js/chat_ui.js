const chat_core = new ChatEngine();

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
    }
    
    if (from === FROM.USER) {
        const user_chat_element = `<article class="message sechuv-user"><div class="message-body sechuv-user-body">${message}</div></article>`;
        chat_div.append(user_chat_element);
    }
    
    $("html,body").animate({scrollTop:$($('.message')[$('.message').length-1]).offset().top});
}

const input_chat = (e) => {
    if(chat_input.val()){
        const user_input = chat_input.val();

        add_chat(FROM.USER, user_input);
        chat_input.val(""); 

        setTimeout(() => add_chat(FROM.BOT, chat_core.generate_message(user_input)), 500);
    }
    e.preventDefault();
}

chat_form.on("submit", input_chat);