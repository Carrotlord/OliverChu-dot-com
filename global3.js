/** @author Jiangcheng Oliver Chu */

function changeHover(modalButtonId, imageBaseName, shouldHover) {
    var modalButton = document.getElementById(modalButtonId + "ModalButton");
    var imagePrefix = "img/";
    var imageSuffix;
    if (shouldHover) {
        imageSuffix = "_hover.png";
    } else {
        imageSuffix = ".png";
    }
    modalButton.src = imagePrefix + imageBaseName + imageSuffix;
}

function setHover(modalButtonId, imageBaseName) {
    changeHover(modalButtonId, imageBaseName, true);
}

function resetHover(modalButtonId, imageBaseName) {
    changeHover(modalButtonId, imageBaseName, false);
}

function navigateTo(url) {
    window.location = url;
}