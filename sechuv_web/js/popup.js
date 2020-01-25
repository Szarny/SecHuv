let vulntypes = [];

const configureUI = checkResult => {
    if (checkResult.length === 0) {
        $("#result").html(`<span class="tag is-success is-medium">人的脆弱性は検出されませんでした。</span>`);
        $("#report_button").prop("disabled", true);
        return;
    }

    window.alert(`${checkResult.length}件の人的脆弱性が検出されました。`)
    $("#report_button").prop("disabled", false);
    
    for (let vuln of checkResult) {
        vulntypes.push(vuln.vulntype);

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

    const web_post_spec = {
        url: $("#url_input").val()
    };

    const url = "http://localhost:8080/web/check";
    const method = "POST";
    const headers = {
        'Content-Type': 'application/json'
    };
    const body = JSON.stringify(web_post_spec);

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

const report = () => {
    const webcasepost = {
        vulntypes: vulntypes,
        spec: {
            url: $("#url_input").val()
        }
    }

    const url = "http://localhost:8080/web/case";
    const method = "POST";
    const headers = {
        'Content-Type': 'application/json'
    }
    const body = JSON.stringify(webcasepost);

    fetch(url, {
        method,
        headers,
        body
    }).then(res => {
        return res.json();
    }).then(json => {
        return json.uuid;
    }).then(uuid => {
        chrome.tabs.create({url: `http://localhost:8000/web/${uuid}`});
    })
}

$("#current_url_button").on("click", e => {
    chrome.tabs.getSelected(null, tab => {
        $("#url_input").val(tab.url);
    });
})

$("#check_button").on("click", e => {
    check();
})

$("#report_button").on("click", e => {
    report();
})