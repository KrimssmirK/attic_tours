$(document).ready(() => {
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
                alert('Sorry, there was a problem with fetching queues!')
                console.log('Error: ' + errorThrown)
                console.log('Status: ' + status)
                console.dir(xhr)
            })
            return [data.queues, data.windows]
        }

        // construct queue card (component)
        function construct_queue_card(queue, window) {

            $queue_card =
                $("<div>", {
                    class: "rounded p-0 m-0 w-100 mh-100",
                    style: "border: 5px solid #FF0000;"
                }).append(
                    $("<div>", {
                        class: "d-flex flex-column justify-content-between p-1",
                        style: "overflow: hidden;position: relative;white-space: nowrap;"
                    }
                    ).append(
                        $("<div>", {
                            class: "text-white text-center rounded p-1",
                            style: "background-color: #FF0000;"
                        }).append(
                            $("<span>", {
                                class: "fw-bold",
                                style: "font-size: 1.3vw;",
                                text: queue.service_name
                            })
                        )
                    ).append(
                        $("<span>", {
                            id: "queue_no_" + queue.id,
                            class: "fw-bold text-center",
                            style: "font-size:8vw;",
                            text: queue.current_no
                        })
                    ).append(
                        $("<div>", {
                            class: "text-center"
                        }).append(
                            $("<span>", {
                                id: "queue_window_" + queue.id,
                                class: "fw-bold",
                                style: "font-size: 1.2vw;",
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

                console.log("ring functions queue: ", queue)

                // queue card info
                const template = queue.service_name + " applicant number " + $("#queue_no_" + queue.id).text() + " please proceed to " + $("#queue_window_" + queue.id).text()

                const message = new SpeechSynthesisUtterance(template)
                // message settings
                if (voice_selected) {
                    message.voice = voice_selected
                }
                message.volume = 1
                message.pitch = 1.3
                message.rate = 0.8
                message.lang = "en-US"



                // speak
                speechSynthesis.speak(message)
            }

            function call() {

                $("#audio_calling")[0].play().then(_ => {
                    // Autoplay started!
                    const delayInMilliseconds = 3_000
                    setTimeout(() => speak(), delayInMilliseconds);
                }).catch(error => {
                    console.log("Error in Audio")
                    console.log(error)
                });
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
                            alert('Sorry, there was a problem with fetching queues!')
                            console.log('Error: ' + errorThrown)
                            console.log('Status: ' + status)
                            console.dir(xhr)
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
                        alert('Sorry, there was a problem with updating queue..')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
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

    init_queue_cards()
})

