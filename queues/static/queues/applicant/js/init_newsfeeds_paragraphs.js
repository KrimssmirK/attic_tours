// this is run when the document is fully loaded
$(document).ready(() => {

    // initialize the newsfeed for applicant's view
    init_newsfeeds_paragraphs(branch_id) // param: branch_id is a global variable


    async function init_newsfeeds_paragraphs(branch_id) { // branch_id is global variable

        const SIZE_LETTER_IN_VW = 2

        async function request_newsfeeds() {
            const WINDOW = window
            const ENDPOINT = WINDOW.location.origin + '/branch/api/newsfeeds/'
            var data = await $.ajax({
                url: ENDPOINT,
                type: 'GET',
                data: { "branch_id": branch_id }
            }).fail((xhr, status, errorThrown) => {
                console.log('Error: ' + errorThrown)
                console.log('Status: ' + status)
                console.dir(xhr)
                // browser reloads the page if the connection is failed due to slow internet connection
                WINDOW.location.reload()
            })
            return data.newsfeeds
        }


        function create_newsfeed(text) {
            const properties = {
                class: "p-2 fw-bold text-white user-select-none",
                style: "font-size:" + String(SIZE_LETTER_IN_VW) + "vw;",
                text: text,
            }
            return $("<p>", properties)
        }


        // ----------------------------------------init newsfeed paragraphs----------------------------------------
        var newsfeeds = await request_newsfeeds()
        // appending paragraph (p)
        let nletters = 0
        let n_groups = 0
        newsfeeds.forEach(newsfeed => {
            $newsfeed_paragraph = create_newsfeed(newsfeed.text)
            $("#newsfeeds-container").append($newsfeed_paragraph)
            nletters += newsfeed.text.length
            n_groups += 1
        })
        // ----------------------------------------init newsfeed paragraphs (END)-----------------------------------










        // ---------------------------------------ANIMATIONS SETTINGS-----------------------------------------------
        const ADJUST = 1.5
        const LEFT = ((4 + nletters) + (5 * n_groups)) * ADJUST
        const SPEED = 0.005
        const DURATION = LEFT / SPEED
        setInterval(() => {
            $("#newsfeeds-container").animate(
                {
                    left: "-" + String(LEFT) + "%"
                },
                {
                    duration: DURATION,
                    easing: "linear",
                    complete: () => {
                        $("#newsfeeds-container").css("left", "100%")
                    }
                }
            )
        })
    }
})