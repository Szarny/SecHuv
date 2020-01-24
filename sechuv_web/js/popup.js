const configureUI = checkResult => {
    if (checkResult.length === 0) {
        $("#result").html(`<span class="tag is-success is-medium">人的脆弱性は検出されませんでした。</span>`);
        $("#report_button").prop("disabled", true);
        return;
    }

    window.alert(`${checkResult.length}件の人的脆弱性が検出されました。`)
    $("#report_button").prop("disabled", false);
    
    for (let vuln of checkResult) {
        $("#result").html(`<button class="tag is-danger is-medium" id="tag-${vuln.vulntype}">${vuln.vulntype}</button>`);
        $(`#tag-${vuln.vulntype}`).on("click", {
            url: `http://localhost:8000/vuln/${vuln.vulntype}`
        }, e => {
            chrome.windows.create({
                url: e.data.url
            });
        });
    }
}

const check = () => {
    $("#result").html(`<progress class="progress is-small is-primary" max="100">15%</progress>`);

    const webspec = {
        url: $("#url_input").val(),
        body: $("#body_html").val(),
        raw_body: $("#body_text").val(),
        screenshot: ""
    };

    const url = "http://localhost:8080/web/check";
    const method = "POST";
    const headers = {
        'Content-Type': 'application/json'
    };
    const body = JSON.stringify(webspec);

    fetch(url, {
        method,
        headers,
        body
    }).then(res => {
        return res.json();
    }).then(json => {
        configureUI(json);
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
            $("#body_html").val(result);
            chrome.tabs.query({
                active: true,
                currentWindow: true
            }, tabs => {
                const tab = tabs[0];
                chrome.tabs.executeScript(tab.id, {
                    code: 'document.body.innerText'
                }, result => {
                    $("#body_text").val(result);
                    check();
                });
            });
        });
    });
})