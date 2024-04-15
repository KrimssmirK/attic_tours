const queue_interval = setInterval(() => {
    if (NUMBER_API_QUEUE_CALLS > Object.keys(UiState).length) {
        $("#loading").detach()
        function produce_html(service) {
            const service_mod = service.replaceAll(" ", "_")
            return `
                <div class="m-1" style="width:320px;">
                    <div class="container-fluid border border-2 border-white p-2 shadow" style="background-color: #D43F3A;">
                      <h2 class="p-2 bg-white text-center fw-bold fs-2" id="${service_mod + "_name"}">${service}</h2>
                      <div class="container-fluid bg-white">
                        <div class="d-flex justify-content-between align-items-center">
                          <i class="bi bi-chevron-compact-left fs-1" style="cursor: pointer;" id=${service_mod + "_left_arrow"}></i>
                          <p class="fw-bold text-center m-0" style="font-size:120px;" id=${service_mod + "_queue_number"}>${UiState[service].number}</p>
                          <i class="bi bi-chevron-compact-right fs-1" style="cursor: pointer;" id=${service_mod + "_right_arrow"}></i>
                        </div>
                      </div>
                      <select class="text-center fw-bold p-2 mt-2" style="width: 100%; font-size: 20px;" id=${service_mod + "_window_number"} name="windows">
                        <option value="0">WINDOW: ANY</option>
                        <option value="1">WINDOW 1</option>
                        <option value="2">WINDOW 2</option>
                        <option value="3">WINDOW 3</option>
                        <option value="4">WINDOW 4</option>
                        <option value="5">WINDOW 5</option>
                        <option value="6">WINDOW 6</option>
                        <option value="7">WINDOW 7</option>
                        <option value="8">WINDOW 8</option>
                        <option value="9">WINDOW 9</option>
                        <option value="10">WINDOW 10</option>
                        <option value="11">WINDOW 11</option>
                        <option value="12">WINDOW 12</option>
                      </select>
                    </div>
                    <div class="text-center py-2">
                      <button type="button" class="text-white fw-bold w-100" style="font-size: 40px; background-color: #D43F3A;" id=${service_mod + "_call"}>CALL</button>
                    </div>
                  </div>
                `
        }

        function set_functionality(service) {
            const service_mod = service.replaceAll(" ", "_")
            function call_api(endpoint) {
                $.ajax({
                    url: endpoint,
                    type: "GET",
                    dataType: "json",
                })
                    .done((json) => {
                        console.log("SUCCESS")
                    })
                    .fail((xhr, status, errorThrown) => {
                        alert("Sorry, there was a problem!")
                        console.log("Error: " + errorThrown)
                        console.log("Status: " + status)
                        console.dir(xhr)
                    })
            }

            $("#" + service_mod + "_left_arrow").click(() => {
                const ENDPOINT = window.location.origin + "/branch/queues/api/change_number_queue/" + UiState[service].id + "/" + "-1"
                call_api(ENDPOINT)
                const current_value = $("#" + service_mod + "_queue_number").html()
                if (Number(current_value) > 0) {
                    UiState[service].number -= 1
                    $("#" + service_mod + "_queue_number").html(String(Number(current_value) - 1))
                }
            })
            $("#" + service_mod + "_right_arrow").click(() => {
                const ENDPOINT = window.location.origin + "/branch/queues/api/change_number_queue/" + UiState[service].id + "/" + "1"
                call_api(ENDPOINT)
                const current_value = $("#" + service_mod + "_queue_number").html()
                UiState[service].number += 1
                $("#" + service_mod + "_queue_number").html(String(Number(current_value) + 1))
            })
            $("#" + service_mod + "_window_number").on("change", () => {
                const value = $("#" + service_mod + "_window_number" + " option:selected").val()
                UiState[service].window = Number(value)
                $("#" + service_mod + "_window_number" + " option:selected").val(value)
                const ENDPOINT = window.location.origin + "/branch/queues/api/change_window_queue/" + UiState[service].id + "/" + value
                call_api(ENDPOINT)
            })
            $("#" + service_mod + "_call").click(() => {
                const ENDPOINT = window.location.origin + "/branch/queues/api/change_call_queue/" + UiState[service].id + "/" + "on"
                call_api(ENDPOINT)
            })
        }

        function update_ui_constantly(service) {
            setInterval(() => {
                const service_mod = service.replaceAll(" ", "_")
                $("#" + service_mod + "_queue_number").html(UiState[service].number)
                $("#" + service_mod + "_window_number").val(UiState[service].window)
            }, 1_000)
        }

        SERVICES.forEach((SERVICE) => {
            $("#queue_container").append(produce_html(SERVICE))
            set_functionality(SERVICE)
            update_ui_constantly(SERVICE)
        });

        clearInterval(queue_interval)
    }
}, 1_000)