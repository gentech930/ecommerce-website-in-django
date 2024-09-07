document.addEventListener('DOMContentLoaded', function () {
    // Dropdown on mouse hover
    function toggleNavbarMethod() {
        if (window.innerWidth > 992) {
            document.querySelectorAll('.navbar .dropdown').forEach(dropdown => {
                dropdown.addEventListener('mouseover', () => {
                    const toggle = dropdown.querySelector('.dropdown-toggle');
                    if (toggle) toggle.click();
                });
                dropdown.addEventListener('mouseout', () => {
                    const toggle = dropdown.querySelector('.dropdown-toggle');
                    if (toggle) {
                        toggle.click();
                        toggle.blur();
                    }
                });
            });
        } else {
            document.querySelectorAll('.navbar .dropdown').forEach(dropdown => {
                dropdown.removeEventListener('mouseover', () => {
                    const toggle = dropdown.querySelector('.dropdown-toggle');
                    if (toggle) toggle.click();
                });
                dropdown.removeEventListener('mouseout', () => {
                    const toggle = dropdown.querySelector('.dropdown-toggle');
                    if (toggle) {
                        toggle.click();
                        toggle.blur();
                    }
                });
            });
        }
    }
    toggleNavbarMethod();
    window.addEventListener('resize', toggleNavbarMethod);

    // Back to top button
    const backToTopButton = document.querySelector('.back-to-top');
    window.addEventListener('scroll', () => {
        backToTopButton.style.display = window.scrollY > 100 ? 'block' : 'none';
    });
    backToTopButton.addEventListener('click', event => {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Product Quantity
    document.querySelectorAll('.quantity button').forEach(button => {
        button.addEventListener('click', () => {
            const input = button.parentElement.parentElement.querySelector('input');
            let oldValue = parseFloat(input.value);
            input.value = button.classList.contains('btn-plus') ? oldValue + 1 : Math.max(oldValue - 1, 0);
        });
    });
});
