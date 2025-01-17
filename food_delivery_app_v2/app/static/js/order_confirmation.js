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
        // Ensure we only add one event listener
        printButton.onclick = function(e) {
            e.preventDefault();
            window.print();
        };
    }
    // Print functionality for the existing button
    // const printButton = document.getElementById('printButton');
    // if (printButton) {
    //     printButton.addEventListener('click', function () {
    //         // Save original styles of elements
    //         const otherElements = document.querySelectorAll('body > *:not(.payment-confirmation)');
    //         const originalStyles = [];

    //         otherElements.forEach((el, index) => {
    //             originalStyles[index] = el.style.display; // Save current display style
    //             el.style.display = 'none'; // Hide all other elements
    //         });

    //         // Trigger print
    //         window.print();

    //         // Restore original styles
    //         otherElements.forEach((el, index) => {
    //             el.style.display = originalStyles[index]; // Restore display style
    //         });
    //     });
    // }
});