const navpanel = document.getElementById('Nav-Panel');
const toggle = document.getElementById('toggle');
toggle.onclick = function () {
    toggle.classList.toggle('active');
    navpanel.classList.toggle('active');
}