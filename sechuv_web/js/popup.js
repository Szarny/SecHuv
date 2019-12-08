const check = () => {
    const webspec = {
        url: $("#url_input").val(),
        body: $("#body_innerHTML").val(),
        raw_body: $("#body_outerHTML").val()
    }

    const url = "http://localhost:8080/web/check";
    const method = "POST";
    const headers = {
        'Content-Type': 'application/json'
    };
    const body = JSON.stringify(webspec);

    fetch(url, {method, headers, body}).then(res => {
        return res.json()
    }).then(json => {
        $("#result").text(JSON.stringify(json));
    })
}

$("#current_url_button").on("click", e => {
    chrome.tabs.getSelected(null, tab => {
        $("#url_input").val(tab.url);
    });
})

$("#check_button").on("click", e => {
    chrome.tabs.query({
        active: true,
        currentWindow: true
    }, tabs => {
        const tab = tabs[0];
        chrome.tabs.executeScript(tab.id, {
            code: 'document.body.innerHTML'
        }, result => {
            $("#body_innerHTML").val(result);
            chrome.tabs.query({
                active: true,
                currentWindow: true
            }, tabs => {
                const tab = tabs[0];
                chrome.tabs.executeScript(tab.id, {
                    code: 'document.body.outerHTML'
                }, result => {
                    $("#body_outerHTML").val(result);
                    check();
                });
            });
        });
    });
})