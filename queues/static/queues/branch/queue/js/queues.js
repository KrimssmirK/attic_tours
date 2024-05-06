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

        const DECREASE_QUEUE_NO = 0
        const INCREASE_QUEUE_NO = 1
        const SET_WINDOW = 2
        const CALL_APPLICANT = 3

        function post_request(types_of_request, data) {
            const ENDPOINTS = {
                0: "/branch/api/decrease_queue_no/",
                1: "/branch/api/increase_queue_no/",
                2: "/branch/api/set_queue_window/",
                3: "/branch/api/call_applicant/"
            }
            console.log(window.location.origin + ENDPOINTS[types_of_request])
            $.ajax({
                type: 'POST',
                dataType: 'json',
                data: data,
                url: window.location.origin + ENDPOINTS[types_of_request],
            })
                .done((data) => {
                    // console.log(data)
                    // alert(data.status)
                })
                .fail((xhr, status, errorThrown) => {
                    alert('Sorry, there was a problem with changing a queue!')
                    console.log('Error: ' + errorThrown)
                    console.log('Status: ' + status)
                    console.dir(xhr)
                })

        }
        // WINDOW
        $windows = $("<select>", {
            id: "queue_window_id_" + queue.id,
            class: "text-center fw-bold p-2 mt-2 border-0",
            style: "width: 100%; font-size: 18px; cursor: pointer;",
            name: "windows"
        }).on("change", () => {
            // ------------------------HERE------------------------
            var window_id = $("#queue_window_id_" + queue.id).val()
            post_request(
                SET_WINDOW,
                data = {
                    "queue_id": queue.id,
                    "window_id": window_id
                }
            )
        })
        windows.forEach(window => {
            $windows.append(
                $("<option>", {
                    value: window.id,
                    text: window.name,
                    selected: window.id == queue.current_window_id
                })
            )
        })

        // queue - service_name, current_no
        // QUEUE
        const TITLE_LENGTH = queue.service_name.length
        let size_of_title = TITLE_LENGTH > 12 ? 12 : 24
        return $("<div>", {style: "width:250px;height:300px;" })
            .append(
                $("<div>",
                    {
                        id: "queue_card_no_" + queue.id + "_upper",
                        class: "border border-2 border-white p-2 shadow",
                        style: "background-color: #D43F3A; opacity: 0.85;",
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
                            }).on("click", () => {
                                // ---------------------------HERE--------------------------------
                                var current_no = $("#queue_number_id_" + queue.id).text()
                                if (Number(current_no) > 0) {
                                    current_no = Number(current_no) - 1
                                    post_request(
                                        DECREASE_QUEUE_NO,
                                        data = {
                                            "queue_id": queue.id,
                                            "current_no": current_no
                                        }
                                    )
                                }
                                $("#queue_number_id_" + queue.id).text(current_no)
                            })
                        ).append(
                            $("<p>", {
                                id: "queue_number_id_" + queue.id,
                                class: "fw-bold text-center m-0",
                                style: "font-size:100px;",
                                text: queue.current_no
                            })
                        ).append(
                            $("<i>", {
                                class: "bi bi-chevron-compact-right fs-4",
                                style: "cursor: pointer;"
                            }).on("click", () => {
                                // ---------------------------HERE--------------------------------
                                var current_no = $("#queue_number_id_" + queue.id).text()
                                var current_no = Number(current_no) + 1
                                $("#queue_number_id_" + queue.id).text(current_no)
                                post_request(
                                    INCREASE_QUEUE_NO,
                                    data = {
                                        "queue_id": queue.id,
                                        "current_no": current_no
                                    }
                                )
                            })
                        )
                    )
                ).append(
                    $windows
                )
            ).append(
                $("<div>", { id: "queue_card_no_" + queue.id + "_bottom",class: "text-center py-2", style: "opacity: 1.0;"})
                    .append(
                        $("<button>", {
                            type: "button",
                            class: "text-white fw-bold w-100 border-white border-2",
                            style: "font-size: 24px;background-color: #D43F3A;",
                            text: "CALL"
                        }).on("click", () => {
                            post_request(
                                CALL_APPLICANT,
                                data = {
                                    "queue_id": queue.id
                                }
                            )
                        })
                    )
            ).hover(() => {
                $("#queue_card_no_" + queue.id + "_upper" + ",#queue_card_no_" + queue.id + "_bottom").css("opacity", "1.0")
            }, () => {
                $("#queue_card_no_" + queue.id + "_upper" + ",#queue_card_no_" + queue.id + "_bottom").css("opacity", "0.85")
            })
    }
})