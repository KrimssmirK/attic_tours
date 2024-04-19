function logout() {
    sessionStorage.removeItem("access_token")
    const url = window.location.origin
    open(url, '_self')
}