let BRANCH_LOADED = false
load_branches = () => {
    const URL = window.location.href + "api/branches/"
    $.ajax({
        url: URL,
        type: "GET",
        dataType: "json",
    })
        .done((branches) => {
            branches.forEach((branch) => {
                BRANCHES.push(branch.name)
            })
            BRANCH_LOADED = true
        })
        .fail((xhr, status, errorThrown) => {
            alert("Sorry, there was a problem!")
            console.log("Error: " + errorThrown)
            console.log("Status: " + status)
            console.dir(xhr)
        })
}

load_branches()
