function openToast(
    toastId,
    toastTitle,
    linkURL,
    toastDescription
) {
    let toastTitleEl = document.getElementById("toastTitle");
    toastTitleEl.innerText = toastTitle;

    let toastLinkEl = document.getElementById("toastLink");
    toastLinkEl.innerText = toastDescription;
    toastLinkEl.href = linkURL;

    let toastElement = document.getElementById(toastId);
    let toast = bootstrap.Toast.getOrCreateInstance(toastElement);
    toast.show();
}

function openRegisterAndCloseLogin() {
    let loginOffCanvasElement = document.getElementById("registerOffcanvas");
    let loginOffCanvas = new bootstrap.Offcanvas(loginOffCanvasElement);
    loginOffCanvas.show();
}
