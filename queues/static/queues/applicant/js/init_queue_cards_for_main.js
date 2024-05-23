const ORIGIN = window.location.origin
$(document).ready(() => {
    init_queue_cards()

    async function init_queue_cards() {
        // data
        const queues_and_windows = await request_queues_and_windows()
        const queues = queues_and_windows[0]
        const windows = queues_and_windows[1]
        // construct UI based on the data
        queues.forEach(queue => {
            // get the current selected window
            const window = windows[queue.current_window_id - 1]
            // construct the queue card
            $queue_card = construct_queue_card(queue, window)
            // append to the container in HTML
            $("#queue_card_container").append($queue_card)
        })
    }

    // request queues and windows to the server
    async function request_queues_and_windows() {
        const ENDPOINT = '/branch/api/read_queues/'
        const URL = ORIGIN + ENDPOINT
        const branch_id = Number(window.location.pathname.split('/')[2])
        const data = await $.ajax({
            type: 'GET',
            dataType: 'json',
            data: { "branch_id": branch_id },
            url: URL,
        }).fail((xhr, status, errorThrown) => {
            alert('Sorry, there was a problem with fetching queues and windows!')
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
                id: "border_"+queue.id,
                class: "rounded p-0 m-0 w-100 mh-100",
                style: "border: 3px solid #000000;"
            }).append(
                $("<div>", {
                    class: "d-flex flex-column justify-content-between p-1",
                    style: "overflow: hidden;position: relative;white-space: nowrap;"
                }
                ).append(
                    $("<div>", {
                        id: "title_panel_"+queue.id,
                        class: "text-white text-center rounded p-1",
                        style: "background-color: #000000;"
                    }).append(
                        $("<p>", {
                            id: "title_" + queue.id,
                            class: "fw-bold user-select-none m-0",
                            style: "font-size: 1.4vw;",
                            text: queue.service_name
                        })
                    )
                ).append(
                    $("<p>", {
                        id: "queue_no_" + queue.id,
                        class: "fw-bold text-center user-select-none m-0",
                        style: "font-size:9vw;color:black;",
                        text: queue.current_no
                    })
                ).append(
                    $("<div>", {
                        class: "text-center"
                    }).append(
                        $("<p>", {
                            id: "queue_window_" + queue.id,
                            class: "fw-bold user-select-none m-0",
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

        function call() {
    
            $("#audio_calling")[0].play().then(_ => {
                // Autoplay started!
                // speak feature is removed by main office
                // const delayInMilliseconds = 3_000
                // setTimeout(() => speak(), delayInMilliseconds);

                // animation feature
                animate()
            }).catch(error => {
                console.log("Error in Audio")
                console.log(error)
            });
        }

        function animate_after() {
            $("#border_" + queue.id).animate({
                borderColor: "red"
            }, "slow")
            $("#title_panel_" + queue.id).animate({
                backgroundColor: "red"
            }, "slow")
            $("#title_" + queue.id).animate({
                fontSize: "1.7vw"
            }, "slow")
            $("#queue_no_" + queue.id).animate({
                color: "red",
                fontSize: "12vw"
            }, "slow")
            $("#queue_window_" + queue.id).animate({
                color: "red",
                fontSize: "1.5vw"
            }, "slow")
        }

        function animate_before() {
            $("#border_" + queue.id).animate({
                borderColor: "black"
            }, "slow")
            $("#title_panel_" + queue.id).animate({
                backgroundColor: "black"
            }, "slow")
            $("#title_" + queue.id).animate({
                fontSize: "1.4vw"
            }, "slow")
            $("#queue_no_" + queue.id).animate({
                color: "black",
                fontSize: "9vw"
            }, "slow")
            $("#queue_window_" + queue.id).animate({
                color: "black",
                fontSize: "1.2vw"
            }, "slow")
        }

        function animate() {
            for (var i = 0 ; i < 4 ; i++) {
                animate_after()
                animate_before()
            }
        }
    
        function speak() {
            const VOICES = speechSynthesis.getVoices()
            let voice_selected = null
            for (const voice of VOICES) {
                if (voice.name == "Samantha") {
                    voice_selected = voice
                }
            }
    
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
})



