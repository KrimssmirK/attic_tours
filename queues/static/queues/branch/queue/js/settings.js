$(document).ready(() => {
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
            $("#select_service").append(
                $("<option value=" + service.id + ">" + service.name + "</option>")
            )
        })
        var pref_queues = await get_preference_queues(branch_id)
        console.log(pref_queues)
        pref_queues.forEach(pref_queue => {
            $("#remove_service").append(
                $("<option value=" + pref_queue.id + ">" + (services[pref_queue.service_id-1]).name + "</option>")
            )
        })
    })()

    // add service button
    $("#add_service").on("click", () => {
        const service_id = $("#select_service").val()
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
})