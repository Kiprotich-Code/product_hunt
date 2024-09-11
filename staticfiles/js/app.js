document.addEventListener('DOMContentLoaded', function () {
    const hackerText = document.querySelector('.large_h');
    let text = hackerText.getAttribute('data-text');
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            hackerText.innerHTML += text[index];
            index++;
            setTimeout(typeEffect, 100);
        }
    }

    hackerText.innerHTML = '';
    typeEffect();
});
