temp_queues_data = {
    "queues": [
        {
            "service_name": "Japan Visa",
            "current_no": 14,
        },
        {
            "service_name": "Korean Visa",
            "current_no": 3,
        },
        {
            "service_name": "TICKET",
            "current_no": 10,
        },
        {
            "service_name": "Japan Visa",
            "current_no": 14,
        },
        {
            "service_name": "Korean Visa",
            "current_no": 3,
        },
        {
            "service_name": "TICKET",
            "current_no": 10,
        },
    ],
    "windows": [
        { "id": 1, "name": "ANY WINDOW" },
        { "id": 2, "name": "WINDOW 1" },
        { "id": 3, "name": "WINDOW 2" },
        { "id": 4, "name": "WINDOW 3" },
        { "id": 5, "name": "WINDOW 4" },
        { "id": 6, "name": "WINDOW 5" },
        { "id": 7, "name": "WINDOW 6" },
        { "id": 8, "name": "WINDOW 7" },
        { "id": 9, "name": "WINDOW VISA" },
        { "id": 10, "name": "WINDOW JAPAN VISA" },
        { "id": 11, "name": "WINDOW KOREA VISA" },
        { "id": 12, "name": "WINDOW TICKETING" },
        { "id": 13, "name": "WINDOW TOUR PACKAGE" },
        { "id": 14, "name": "WINDOW WIFI" },
        { "id": 15, "name": "WINDOW TOUR PACKAGE" },
    ]
}

$(document).ready(() => {
    // generate queue card based on number of queues data
    let ENDPOINT = window.location.origin + '/branch/api/read_queues/'
    $.ajax({
        type: 'GET',
        dataType: 'json',
        data: { "branch_id": branch_id },
        url: ENDPOINT,
    })
        .done((data) => {
            data.queues.forEach(queue => {
                $("#queue_card_container").append(create_queue_card(queue, data.windows))
            })
        })
        .fail((xhr, status, errorThrown) => {
            alert('Sorry, there was a problem with fetching queues!')
            console.log('Error: ' + errorThrown)
            console.log('Status: ' + status)
            console.dir(xhr)
        })

    function create_queue_card(queue, windows) {
        // WINDOW
        $windows = $("<select>", {
            class: "text-center fw-bold p-2 mt-2 border-0",
            style: "width: 100%; font-size: 18px; cursor: pointer;",
            name: "windows"
        })

        windows.forEach(window => {
            $windows.append(
                $("<option>", {
                    value: window.id,
                    text: window.name
                })
            )
        })
        // queue - service_name, current_no
        // QUEUE
        const TITLE_LENGTH = queue.service_name.length
        let size_of_title = TITLE_LENGTH > 12 ? 12 : 24
        return $("<div>", { style: "width:250px;height:300px;" })
            .append(
                $("<div>",
                    {
                        class: "border border-2 border-white p-2 shadow",
                        style: "background-color: #D43F3A;",
                    }
                ).append(
                    $("<h3>", {
                        class: "p-2 bg-white text-center fw-bold",
                        style: "font-size: " + size_of_title + "px; height: 45px;white-space: nowrap; overflow: hidden;text-overflow: ellipsis;",
                        text: queue.service_name
                    })
                ).append(
                    $("<div>", {
                        class: "bg-white p-0"
                    }
                    ).append(
                        $("<div>", {
                            class: "d-flex justify-content-between align-items-center"
                        }
                        ).append(
                            $("<i>", {
                                class: "bi bi-chevron-compact-left fs-4",
                                style: "cursor: pointer;"
                            })
                        ).append(
                            $("<p>", {
                                class: "fw-bold text-center m-0",
                                style: "font-size:100px;",
                                text: queue.current_no
                            })
                        ).append(
                            $("<i>", {
                                class: "bi bi-chevron-compact-right fs-4",
                                style: "cursor: pointer;"
                            })
                        )
                    )
                ).append(
                    $windows
                )
            ).append(
                $("<div>", { class: "text-center py-2" })
                    .append(
                        $("<button>", {
                            type: "button",
                            class: "text-white fw-bold w-100 border-white border-2",
                            style: "font-size: 24px;background-color: #D43F3A;",
                            text: "CALL"
                        })
                    )
            )
    }
})

{/* <div style="width:200px;height:300px;"> DONE
      <div class="container-fluid border border-2 border-white p-2 shadow" style="background-color: #D43F3A;"> DONE
        <h3 class="p-2 bg-white text-center fw-bold" style="font-size: 24px;">JAPAN VISA</h3>
        <div class="container-fluid bg-white p-0">
          <div class="d-flex justify-content-between align-items-center">
            <i class="bi bi-chevron-compact-left fs-4" style="cursor: pointer;"></i>
            <p class="fw-bold text-center m-0" style="font-size:100px;">4</p>
            <i class="bi bi-chevron-compact-right fs-4" style="cursor: pointer;"></i>
          </div>
        </div>
        <select class="text-center fw-bold p-2 mt-2 border-0" style="width: 100%; font-size: 18px;" name="windows">
          <option value="0">WINDOW: ANY</option>
        </select>
      </div>
      <div class="text-center py-2">
        <button type="button" class="text-white fw-bold w-100 border-white border-2" style="font-size: 24px;background-color: #D43F3A;">CALL</button>
      </div>
    </div> */}

