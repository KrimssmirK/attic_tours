get_all_services = (callback1) => {
    var URL = window.location.href + "api/services/"
    $.ajax({
        url: URL,
        type: "GET",
        dataType: "json",
    })
        .done((services) => {
            services.forEach((service)=>{
                SERVICES.push(service.name)
            })
            callback1(SERVICES)
        })
        .fail((xhr, status, errorThrown) => {
            alert("Sorry, there was a problem!")
            console.log("Error: " + errorThrown)
            console.log("Status: " + status)
            console.dir(xhr)
        })
}

initialize_ui_state = (services) => {
    services.forEach((service) => {
        UiState[service] = null    
    })
}

get_all_services(initialize_ui_state)