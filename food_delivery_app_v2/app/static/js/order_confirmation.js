document.addEventListener('DOMContentLoaded', function () {
    // Add animation to the confirmation icon
    const confirmationIcon = document.querySelector('.confirmation-icon svg');
    if (confirmationIcon) {
        confirmationIcon.classList.add('animate');
        confirmationIcon.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
        confirmationIcon.style.transform = 'scale(1.5)';
        confirmationIcon.style.opacity = '1';

        setTimeout(() => {
            confirmationIcon.style.transform = 'scale(1)';
        }, 500);
    }

    // Print functionality
    const printButton = document.getElementById('printButton');
    if (printButton) {
        printButton.onclick = function(e) {
            e.preventDefault();
            window.print();
        };
    }
});
