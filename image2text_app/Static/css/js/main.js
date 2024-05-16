document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.querySelector('nav'); // Assuming all nav-links are within a <nav> element

    navContainer.addEventListener('mouseover', function(event) {
        if (event.target.classList.contains('nav-link')) {
            event.target.classList.add('dimmed');
        }
    });

    navContainer.addEventListener('mouseout', function(event) {
        if (event.target.classList.contains('nav-link')) {
            event.target.classList.remove('dimmed');
        }
    });
});
