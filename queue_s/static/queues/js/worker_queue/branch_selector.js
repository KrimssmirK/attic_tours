const branch_interval = setInterval(() => {
    if (BRANCH_LOADED) {
        const ADJUST = 1
        BRANCHES.forEach((BRANCH, index) => {
            if (index == 0) {
                sessionStorage.setItem("branch_id", index + ADJUST)
            }
            $('#branches').append($('<option>', {
                value: index + ADJUST,
                text: BRANCH
            }));
        });
        $("#branches").on("change", () => {
            const branch_id = $("#branches").val()
            sessionStorage.setItem("branch_id", branch_id)
            $
        })
        clearInterval(branch_interval)
    }
}, 500)