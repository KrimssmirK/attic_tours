$(document).ready(() => {
    $("#logout").hover(
        () => {
            $("#logout").css("opacity", "0.8")
        }, () => {
            $("#logout").css("opacity", "1.0")
        }).on("click", () => {
            sessionStorage.removeItem("access_token");
            const url = window.location.origin;
            open(url, '_self');
        })
})