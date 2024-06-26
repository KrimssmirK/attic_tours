$(document).ready(() => {
    let branchId
    $("#branchLoginModal").on("shown.bs.modal", (event) => {
        // focus when modal entered
        $("#branchLoginModal input#password-entry").focus()
        // get the branch info
        branchId = event.relatedTarget.getAttribute("data-bs-branch-id")
        const branchName = event.relatedTarget.getAttribute("data-bs-branch-name")
        // change the title of the modal opened
        $("#branchLoginModal .modal-title").text(branchName)


    })
    // login logic frontend
    function login(branchId, password) {
        const ENDPOINT = window.location.origin + '/login/'
        $.ajax({
            url: ENDPOINT,
            type: 'POST',
            data: {
                branchId: branchId,
                password: password
            },
            dataType: 'json'
        })
            .done((result) => {
                if (result.password_matched) {
                    sessionStorage.setItem("access_token", result.access_token)
                    const url = window.location.origin + '/branch/' + branchId + "/queue/"
                    open(url, '_self')
                } else {
                    alert('password is incorrect!')
                }
            })
            .fail((xhr, status, errorThrown) => {
                alert('Sorry, there was a problem!')
                console.log('Error: ' + errorThrown)
                console.log('Status: ' + status)
                console.dir(xhr)
            })

    }

    // login with button click
    $(".modal-footer button#login").on("click", () => {
        const password = $('.modal-body input').val()
        login(branchId, password)
        $('.modal-body input').val('')
        $('#branchLoginModal').modal('hide')
    })
    // login with keyboard enter
    $("#password-entry").keypress((event) => {
        if (event.key == "Enter") {
            event.preventDefault()
            const password = $('.modal-body input').val()
            login(branchId, password)
            $('.modal-body input').val('')
            $('#branchLoginModal').modal('hide')
        }
    })
})