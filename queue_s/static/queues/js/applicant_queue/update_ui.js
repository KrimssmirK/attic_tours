speak = () => {
    const service = sessionStorage.getItem("service")
    const queue_number = sessionStorage.getItem("number")
    const window_number = sessionStorage.getItem("window")
    const template = Number(window_number) ? 
    service + "applicant number" + queue_number + "please proceed to window number" + window_number :
    service + "applicant number" + queue_number + "please proceed to any window"
    const message = new SpeechSynthesisUtterance(template)
    message.volume = 1
    message.pitch = 1.5
    message.rate = 0.8
    message.lang = "en-US"
    speechSynthesis.speak(message)
}

ring = () => {
    $("#calling")[0].play()
    
    $("#calling").on("ended", () => {
        speak()
        $("#calling")[0].stop()
        console.log("hello im speaking")
    })
}

call_applicant = (service) => {
    sessionStorage.setItem("service", service)
    sessionStorage.setItem("number", UiState[service].number)
    sessionStorage.setItem("window", UiState[service].window)
    ring()
}

set_off_call = (queue_id) => {
    const URL = window.location.origin + "/queue/api/change_call_queue/" + queue_id + "/off/"
    $.ajax({
        url: URL,
        type: "GET",
        dataType: "json",
    })
        .done((json) => {
            // none
        })
        .fail((xhr, status, errorThrown) => {
            alert("Sorry, there was a problem!")
            console.log("Error: " + errorThrown)
            console.log("Status: " + status)
            console.dir(xhr)
        })
}

setInterval(() => {
    if (NUMBER_API_QUEUE_CALLS > Object.keys(UiState).length) {
        // Japan Visa
        $("#current_japan_queue_number").html(UiState["JAPAN VISA"].number)
        var window_number_to_show = 
        UiState["JAPAN VISA"].window ? 
        "Window " + UiState["JAPAN VISA"].window : 
        "Any Window"
        $("#current_japan_window_number").html(window_number_to_show)

        // calling
        var is_japan_visa_calling = UiState["JAPAN VISA"].call
        if (is_japan_visa_calling) {
            UiState["JAPAN VISA"].call = false
            set_off_call(UiState["JAPAN VISA"].id)
            call_applicant("JAPAN VISA")
        }

        // Korea Visa
        $("#current_korea_queue_number").html(UiState["KOREA VISA"].number)
        var window_number_to_show = 
        UiState["KOREA VISA"].window ? 
        "Window " + UiState["KOREA VISA"].window : 
        "Any Window"
        $("#current_korea_window_number").html(window_number_to_show)

        // calling
        var is_korea_visa_calling = UiState["KOREA VISA"].call
        if (is_korea_visa_calling) {
            UiState["KOREA VISA"].call = false
            set_off_call(UiState["KOREA VISA"].id)
            call_applicant("KOREA VISA")
        }
    }
}, 500)