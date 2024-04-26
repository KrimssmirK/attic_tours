$(document).ready(() => {
    // set services for adding queues
    (async function set_service() {
        async function get_services() {
            const ENDPOINT = window.location.origin + '/branch/api/services/'
            var data =  await $.ajax({
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
        var services = await get_services()
        services.forEach(service => {
            $("#select_service").append(
                $("<option value=" + service.id + ">" + service.name + "</option>")
            )
        });
    })()
})