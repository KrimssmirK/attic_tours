// run this js after the document is fully loaded
$(document).ready(() => {

    async function init_newsfeeds_paragraphs(branch_id) { // branch_id is global variable
        
        function construct_newsfeed_paragraph(text) {
            const properties = {
                class: "p-2 fw-bold text-white",
                style: "font-size:2vw;",
                text: text,
            }
            return $("<p>", properties)
        }

        async function request_newsfeeds() {
            const ENDPOINT = window.location.origin + '/branch/api/newsfeeds/'
            var data = await $.ajax({
                url: ENDPOINT,
                type: 'GET',
                data: { "branch_id": branch_id }
            }).fail((xhr, status, errorThrown) => {
                    alert('fetching newsfeed error')
                    console.log('Error: ' + errorThrown)
                    console.log('Status: ' + status)
                    console.dir(xhr)
                })
            return data.newsfeeds
        }

        var newsfeeds = await request_newsfeeds()
        // appending paragraph (p)
        newsfeeds.forEach(newsfeed => {
            $newsfeed_paragraph = construct_newsfeed_paragraph(newsfeed.text)
            $("#newsfeeds-container").append($newsfeed_paragraph)
        })
    }

    init_newsfeeds_paragraphs(branch_id) // branch_id is global variable
})