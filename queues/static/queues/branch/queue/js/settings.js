$(document).ready(() => {

    function init_queue_settings() {
        // set services for adding queues
        (async function set_service() {
            async function get_services() {
                const ENDPOINT = window.location.origin + '/branch/api/services/'
                var data = await $.ajax({
                    url: ENDPOINT,
                    type: 'GET',
                })
                    .fail((xhr, status, errorThrown) => {
                        alert('GET services error')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })

                return data.services
            }
            async function get_preference_queues(branch_id) {
                const ENDPOINT = window.location.origin + '/branch/api/pref_queues/'
                var data = await $.ajax({
                    url: ENDPOINT,
                    data: { "branch_id": branch_id },
                    type: 'GET',
                })
                    .fail((xhr, status, errorThrown) => {
                        alert('GET services error')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })

                return data.pref_queues
            }
            var services = await get_services()
            services.forEach(service => {
                $("#select_add_service").append(
                    $("<option>", { value: service.id, text: service.name })
                )
            })
            var pref_queues = await get_preference_queues(branch_id)
            if (pref_queues.length > 0) {
                pref_queues.forEach(pref_queue => {
                    $("#select_remove_service").append(
                        $("<option>", { value: pref_queue.id, text: (services[pref_queue.service_id - 1]).name })
                    )
                })
                $("#select_remove_service").attr("style", "font-size: 12px;cursor: pointer;")
            } else {
                $("#select_remove_service").append(
                    $("<option>", { value: 0, text: "NO SERVICE SET" })
                )
            }
           
        })()

        // add service button
        $("#button_add_service").on("click", () => {
            const service_id = $("#select_add_service").val()
            put_new_pref_queue(service_id, branch_id)
            function put_new_pref_queue(service_id, branch_id) {
                $.ajax({
                    type: 'POST',
                    url: window.location.origin + '/branch/api/create_pref_queue/',
                    data: { "service_id": service_id, "branch_id": branch_id },
                    dataType: 'json'
                }) // SUCCESS
                    .done((json) => {
                        alert(json.status)
                        window.location.reload()
                    }) // FAIL
                    .fail((xhr, status, errorThrown) => {
                        alert('Sorry, there was a problem with creating new preference queue!')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })
            }
        })

        // this is the logic when the remove service is clicked!
        $("#button_remove_service").on("click", () => {
            // get the selected preference queue id
            const pref_queue_id = $("#select_remove_service").val()
            if (pref_queue_id > 0) {
                request_delete_pref_queue(pref_queue_id)
            } else {
                alert("There is no service to delete")
            }
            
            function request_delete_pref_queue(pref_queue_id) {
                $.ajax({
                    type: 'POST',
                    dataType: 'json',
                    data: { "pref_queue_id": pref_queue_id },
                    url: window.location.origin + '/branch/api/delete_pref_queue/',
                })
                    .done((json) => {
                        alert(json.status)
                        window.location.reload()
                    })
                    .fail((xhr, status, errorThrown) => {
                        alert('Sorry, there was a problem with deleting a preference queue!')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })
            }
        })
    }

    function init_newsfeed_settings() {
        // set services for adding queues
        (async function set_newsfeed() {
            async function get_newsfeeds(branch_id) {
                const ENDPOINT = window.location.origin + '/branch/api/newsfeeds/'
                var data = await $.ajax({
                    url: ENDPOINT,
                    type: 'GET',
                    data: { "branch_id": branch_id }
                })
                    .fail((xhr, status, errorThrown) => {
                        alert('GET services error')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })
                return data.newsfeeds
            }
            var newsfeeds = await get_newsfeeds(branch_id)
            if (newsfeeds.length > 0) {
                newsfeeds.forEach(newsfeed => {
                    $("#select_edit_newsfeed").append(
                        $("<option>", { value: newsfeed.id, text: newsfeed.text })
                    ).attr("style", "font-size: 12px;cursor: pointer;")
                    $("#select_remove_newsfeed").append(
                        $("<option>", { value: newsfeed.id, text: newsfeed.text })
                    ).attr("style", "font-size: 12px;cursor: pointer;")
                })
            } else {
                $("#select_edit_newsfeed").append(
                    $("<option>", { value: "0", text: "NO NEWSFEED SET" })
                )
                $("#select_remove_newsfeed").append(
                    $("<option>", { value: "0", text: "NO NEWSFEED SET" })
                )
            }

        })()

        // add service button
        $("#button_add_newsfeed").on("click", () => {
            const newsfeed_text = $("#textarea_newsfeed").val()
            if (newsfeed_text.length > 0) {
                put_new_pref_queue(newsfeed_text, branch_id)
            } else {
                alert("please enter the text before adding")
            }
            
            function put_new_pref_queue(newsfeed_text, branch_id) {
                $.ajax({
                    type: 'POST',
                    url: window.location.origin + '/branch/api/create_newsfeed/',
                    data: { "newsfeed_text": newsfeed_text, "branch_id": branch_id },
                    dataType: 'json'
                }) // SUCCESS
                    .done((json) => {
                        alert(json.status)
                        window.location.reload()
                    }) // FAIL
                    .fail((xhr, status, errorThrown) => {
                        alert('Sorry, there was a problem with creating new newsfeed!')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })
            }
        })

        // this is the logic when the remove service is clicked!
        $("#button_remove_newsfeed").on("click", () => {
            // get the selected preference queue id
            const newsfeed_id = $("#select_remove_newsfeed").val()
            if (newsfeed_id > 0) {
                request_delete_pref_queue(newsfeed_id)
            } else {
                alert("There is no newsfeed to remove")
            }

            function request_delete_pref_queue(newsfeed_id) {
                $.ajax({
                    type: 'POST',
                    dataType: 'json',
                    data: { "newsfeed_id": newsfeed_id },
                    url: window.location.origin + '/branch/api/delete_newsfeed/',
                })
                    .done((json) => {
                        alert(json.status)
                        window.location.reload()
                    })
                    .fail((xhr, status, errorThrown) => {
                        alert('Sorry, there was a problem with deleting a newsfeed!')
                        console.log('Error: ' + errorThrown)
                        console.log('Status: ' + status)
                        console.dir(xhr)
                    })
            }
        })
    }

    function init_newsfeed_edit_settings() {
        $("#editNewsfeedModal").on("shown.bs.modal", (event) => {
            var newsfeed_id = $("#select_edit_newsfeed").val() // newsfeed id
            var selected_newsfeed_text = $("#select_edit_newsfeed ").find(":selected").text()
            $("#modal_edit_newsfeed").text(selected_newsfeed_text)
            $("#modal_edit_save_button").on("click", () => {
                var new_text = $("#modal_edit_newsfeed").val()
                request_edit_newsfeed(newsfeed_id, new_text)
                $("#modal_edit_save_button").text("").append(
                    $("<div>", { class: "loader" })
                )
            })
        })
        function request_edit_newsfeed(newsfeed_id, new_text) {
            const ENDPOINT = window.location.origin + '/branch/api/change_newsfeed/'
            $.ajax({
                url: ENDPOINT,
                type: 'POST',
                data: {
                    newsfeed_id: newsfeed_id,
                    new_text: new_text,
                },
                dataType: 'json'
            })
                .done((data) => {
                    // do something when the response back
                    window.location.reload()
                })
                .fail((xhr, status, errorThrown) => {
                    alert('Sorry, there was a problem!')
                    console.log('Error: ' + errorThrown)
                    console.log('Status: ' + status)
                    console.dir(xhr)
                })
            
                function set_loading_to_button() {
                    $("#modal_edit_save_button").text()
                }
        }
    }
    

    init_queue_settings()
    init_newsfeed_settings()
    init_newsfeed_edit_settings()
})




   


   

    
