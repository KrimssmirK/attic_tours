$(document).ready(() => {
    const WINDOW = window
    init_queue_cards()
    async function init_queue_cards() {
        const ORIGIN = window.location.origin
        async function request_queues_and_windows() {
            const ENDPOINT = '/branch/api/read_queues/'
            const URL = ORIGIN + ENDPOINT
            const data = await $.ajax({
                type: 'GET',
                dataType: 'json',
                data: { "branch_id": branch_id }, // branch_id is global variable
                url: URL,
            }).fail((xhr, status, errorThrown) => {
                // alert('Sorry, there was a problem with fetching queues!')
                console.log('Error: ' + errorThrown)
                console.log('Status: ' + status)
                console.dir(xhr)
                // browser reloads the page if the connection is failed due to slow internet connection
                WINDOW.location.reload()
            })
            return [data.queues, data.windows]
        }

        // construct queue card (component)
        function construct_queue_card(queue, window) {

            $queue_card =
                $("<div>", {
                    id: "border_" + queue.id,
                    class: "rounded h-75",
                    style: "border: 5px solid #FF0000;width:20%;"
                }).append(
                    $("<div>", {
                        class: "d-flex flex-column justify-content-between p-1 h-100",
                        style: "overflow: hidden;position: relative;white-space: nowrap;"
                    }
                    ).append(
                        $("<div>", {
                            id: "title_panel_" + queue.id,
                            class: "text-center rounded p-2",
                            style: "background-color: #FF0000;width: 100%;"
                        }).append(
                            $("<p>", {
                                id: "title_" + queue.id,
                                class: "fw-bold w-100 user-select-none m-0",
                                style: "font-size: 1.4em; color: white;",
                                text: queue.service_name
                            })
                        )
                    ).append(
                        $("<p>", {
                            id: "queue_no_" + queue.id,
                            class: "fw-bold text-center user-select-none m-0",
                            style: "font-size:9em;",
                            text: queue.current_no
                        })
                    ).append(
                        $("<div>", {
                            class: "text-center"
                        }).append(
                            $("<p>", {
                                id: "queue_window_" + queue.id,
                                class: "fw-bold user-select-none m-0",
                                style: "font-size: 1.2em;",
                                text: window.name
                            })
                        )
                    )
                )

            function update_queue(new_queue) {
                $("#queue_no_" + queue.id).text(new_queue.current_no)
                $("#queue_window_" + queue.id).text(new_queue.window_name)
            }

            function speak() {
                const VOICES = speechSynthesis.getVoices()
                let voice_selected = null
                for (const voice of VOICES) {
                    if (voice.name == "Samantha") {
                        voice_selected = voice
                    }
                }

                const speech = queue.service_name + " applicant number " + $("#queue_no_" + queue.id).text() + " please proceed to " + $("#queue_window_" + queue.id).text()
                const message = new SpeechSynthesisUtterance(speech)
                if (voice_selected) {
                    message.voice = voice_selected
                }
                message.volume = 1
                message.pitch = 1.3
                message.rate = 0.8
                message.lang = "en-US"
                speechSynthesis.speak(message)
            }

            function call() {
                $("#audio_calling")[0].play().then(_ => {
                    // Autoplay started!
                    do_animation()
                    const delayInMilliseconds = 3_000
                    setTimeout(() => {
                        speak()
                    }, delayInMilliseconds);
                })
                    .catch(error => {
                        console.log("Error in Audio")
                        console.log(error)
                    });
            }
           

            

            function do_animation() {
                function back_to_normal_form() {
                    $("#border_" + queue.id).animate({
                        opacity: "1"
                    }, "slow")
                    $("#queue_no_" + queue.id).animate({
                        fontSize: "9em"
                    }, "slow")
                }
                function change_the_normal_form() {
                    $("#border_" + queue.id).animate({
                        opacity: "0.4"
                    }, "slow")
                    $("#queue_no_" + queue.id).animate({
                        fontSize: "5em"
                    }, "slow")
              
                }
                for (var i = 0 ; i < 5 ; i++) {
                    change_the_normal_form()
                    back_to_normal_form()
                } 
            }

            function call_applicant(new_queue) {

                async function request_reset_call() {
                    const ENDPOINT = '/branch/api/reset_call_applicant/'
                    const URL = ORIGIN + ENDPOINT
                    const done = await $.ajax({
                        type: 'POST',
                        dataType: 'json',
                        data: { "queue_id": queue.id },
                        url: URL,
                    })
                        .done((json) => {
                            return true
                        })
                        .fail((xhr, status, errorThrown) => {
                            // alert('Sorry, there was a problem with fetching queues!')
                            console.log('Error: ' + errorThrown)
                            console.log('Status: ' + status)
                            console.dir(xhr)
                            // browser reloads the page if the connection is failed due to slow internet connection
                            WINDOW.location.reload()
                            return false
                        })
                    return done
                }

                if (new_queue.call && request_reset_call()) {
                    call()
                }
            }

            function keep_update_queue(update_callback, call_callback, interval) {
                async function request_queue() {
                    const ENDPOINT = '/branch/api/get_queue/'
                    const URL = ORIGIN + ENDPOINT
                    const new_queue = await $.ajax({
                        type: 'GET',
                        dataType: 'json',
                        data: { "queue_id": queue.id },
                        url: URL,
                    }).fail((xhr, status, errorThrown) => {
                        // alert('Sorry, there was a problem with updating queue..')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                        // browser reloads the page if the connection is failed due to slow internet connection
                        WINDOW.location.reload()
                    })
                    return new_queue
                }

                setInterval(async () => {
                    const new_queue = await request_queue()
                    update_callback(new_queue)
                    call_callback(new_queue)
                }, interval)
            }

            const UPDATE_INTERVAL = 1_000
            keep_update_queue(update_queue, call_applicant, UPDATE_INTERVAL)

            return $queue_card
        }

        const queues_and_windows = await request_queues_and_windows()
        const queues = queues_and_windows[0]
        const windows = queues_and_windows[1]
        queues.forEach(queue => {
            const window = windows[queue.current_window_id - 1]
            $queue_card = construct_queue_card(queue, window)
            $("#queue_card_container").append($queue_card)
        })
    }
})

