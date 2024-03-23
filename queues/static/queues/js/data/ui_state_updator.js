let NUMBER_API_QUEUE_CALLS = 0

get_queue = (service) => {
    var URL = window.location.href + "api/get_queue/" + service
    $.ajax({
        url: URL,
        type: "GET",
        dataType: "json",
    })
        .done((json) => {
            UiState[service] = json
            NUMBER_API_QUEUE_CALLS += 1
        })
        .fail((xhr, status, errorThrown) => {
            alert("Sorry, there was a problem!")
            console.log("Error: " + errorThrown)
            console.log("Status: " + status)
            console.dir(xhr)
        })
}

function check_ui_state_if_not_null() {
    return Object.keys(UiState).length > 0
}

update_queues = (INTERVAL) => {
    setInterval(() => {
        if (check_ui_state_if_not_null()) {
            SERVICES.forEach((SERVICE) => {
                get_queue(SERVICE)
            })
        }

    }, INTERVAL)
}

update_queues(1_000)