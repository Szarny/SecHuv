const types = {
    web: "web",
    mail: "mail",
    other: "other"
};

const phases = {
    default: "default",
    web_url: "web_url",
    mail_iseml: "mail_iseml",
    mail_emlget: "mail_emlget",
    mail_fromaddr: "mail_fromaddr",
    mail_subject: "mail_subject",
    mail_body: "mail_body",
    other_metadata: "other_metadata",
    other_body: "other_body",
    check: "check"
};


class ChatEngine { 
    constructor() {
        this.type = undefined;
        this.phase = phases.default;

        this.webdata = {
            url: undefined
        };

        this.maildata = {
            eml: undefined,
            from_addr: undefined,
            subject: undefined,
            body: undefined
        };

        this.otherdata = {
            media: "SMS",
            metadata: undefined,
            body: undefined
        }
    }

    gen_default_(user_input) {
        if (user_input.match(/Web|web|ウェブ|サイト/)) {
            this.type = types.web;
            this.phase = phases.web_url;
            return "不審なWebサイトに関する相談ですね。では、そのWebサイトのURLを教えてください。"
        }

        if (user_input.match(/メール|Mail|mail/)) {
            this.type = types.mail;
            this.phase = phases.mail_iseml;
            return "不審なメールに関する相談ですね。では、そのメールをエクスポートしてemlファイル形式でこちらに送信することはできますか？「はい」もしくは「いいえ」でお答えください。"
        }

        if (user_input.match(/メッセージ|SMS/)) {
            this.type = types.other;
            this.phase = phases.other_metadata;
            return "不審なメッセージに関する相談ですね。では、そのメッセージの送信者の情報を教えてください。電話番号やメール等なんでも構いません。"
        }

        return "すみません、相談内容が認識できませんでした。もし、不審なWebサイトに関する相談であれば「Web」、不審なメールに関する相談であれば「メール」、不審なメッセージに関する相談であれば「メッセージ」と送信してください。"
    }

    gen_web_url(user_input) {
        const url = user_input.match(/(https?:\/\/[\x21-\x7e]+)/);

        if (!url) {
            return "URLが検出できませんでした。お手数ですが、再度送信してください。";
        }

        this.webdata.url = url;
        this.phase = phases.check;
        return `${url}ですね。ありがとうございます。検査を行いますので、結果が出るまで少々お待ちください。`;
    }

    gen_is_eml(user_input) {
        if (user_input.match(/はい/)) {
            this.phase = phases.mail_emlget;
            return "ありがとうございます。では、emlファイルの内容を送信してください。";
        } 

        if (user_input.match(/いいえ/)) {
            this.phase = phases.mail_fromaddr;
            return "かしこまりました。では、そのメールの送信元メールアドレスを教えてください。。";
        } 
    }

    gen_emlget(user_input) {
        this.maildata.eml = user_input;
        this.phase = phases.check;
        return "ありがとうございます。検査を行いますので、結果が出るまで少々お待ちください。";
    }

    gen_mail_fromaddr(user_input) {
        this.maildata.from_addr = user_input;
        this.phase = phases.mail_subject;
        return "ありがとうございます。では次に、メールの題名を送信してください。";
    }

    gen_mail_subject(user_input) {
        this.maildata.subject = user_input;
        this.phase = phases.mail_body;
        return "ありがとうございます。では次に、メールの本文を送信してください。";
    }

    gen_mail_body(user_input) {
        this.maildata.body = user_input;
        this.phase = phases.check;
        return "ありがとうございます。検査を行いますので、結果が出るまで少々お待ちください。";
    }

    gen_other_metadata(user_input) {
        this.otherdata.metadata = user_input;
        this.phase = phases.other_body;
        return "ありがとうございます。では次に、受信したメッセージ本文を送信してください。";
    }

    gen_other_body(user_input) {
        this.otherdata.body = user_input;
        this.phase = phases.check;
        return "ありがとうございます。検査を行いますので、結果が出るまで少々お待ちください。";
    }

    check() {
        switch(this.type) {
            case types.web:
                break;
            case types.mail:
                break;
            case types.other:
                break;
        }

        if (true /* 結果 */) {
            this.gen_valid();
        } else {
            this.gen_vuln();
        }
    }

    gen_valid() {
        add_chat(FROM.BOT, "検査の結果、不審な点は発見されませんでした。");
        add_chat(FROM.BOT, "もし不安な点があれば、第三者に相談してみたり、<a href='/'>SecHuvの情報</a>を参考にして、慎重に行動してください。");
    }

    gen_vuln() {
        add_chat(FROM.BOT, "検査の結果、送信された内容から人的脆弱性をついた攻撃と思わしき兆候が検出されました。検出された項目は以下の通りです。");
        // TODO: ほげほげ

        switch(this.type) {
            case types.web:
                add_chat(FROM.BOT, "本サイトは上記の人的脆弱性を狙ったフィッシングサイトである恐れがあります。本サイトから直接個人情報等を入力したりせず、検索エンジンやブックマーク等から正規のサイトへとアクセスするようにしてください。");
                break;
            case types.mail:
                add_chat(FROM.BOT, "本メールは上記の人的脆弱性を狙ったフィッシングメールである恐れがあります。本メールに添付されているデータを開いたり、本文に記載されているURLにアクセスしたりしないでください。");
                break;
            case types.other:
                add_chat(FROM.BOT, "本メッセージは上記の人的脆弱性を狙ったものである恐れがあります。本メッセージに関連するデータを開いたり、本文に記載されているURLにアクセスしたりしないでください。");
                break;
        }
    }

    generate_message(user_input) {
        let return_message;

        switch(this.phase) {
            case phases.default:
                return_message = this.gen_default_(user_input);
                break;

            case phases.web_url:
                return_message = this.gen_web_url(user_input);
                break;

            case phases.is_eml:
                return_message = this.gen_is_eml(user_input);
                break;

            case phases.is_emlget:
                return_message = this.gen_emlget(user_input);
                break;

            case phases.mail_fromaddr:
                return_message = this.gen_mail_fromaddr(user_input);
                break;

            case phases.mail_subject:
                return_message = this.gen_mail_subject(user_input);
                break;

            case phases.mail_body:
                return_message = this.gen_mail_body(user_input);
                break;

            case phases.other_metadata:
                return_message = this.gen_other_metadata(user_input);
                break;

            case phases.other_body:
                return_message = this.gen_other_body(user_input);
                break;
        }

        return return_message;
    }
}