// Search functionality
document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('location-input');
    const searchButton = locationInput.nextElementSibling;

    searchButton.addEventListener('click', function() {
        const location = locationInput.value;
        if (location) {
            // Add your search logic here
            window.location.href = `/restaurants?location=${encodeURIComponent(location)}`;
        }
    });

    // Auto-complete for location input
    let autocomplete;
    if (window.google && window.google.maps) {
        autocomplete = new google.maps.places.Autocomplete(locationInput, {
            types: ['geocode']
        });
    }
});

// Lazy loading for images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add to favorites functionality
function toggleFavorite(restaurantId) {
    // Add your favorite toggle logic here
    const favoriteIcon = document.querySelector(`#favorite-${restaurantId}`);
    favoriteIcon.classList.toggle('active');
}

// Restaurant filter functionality
function filterRestaurants(cuisine) {
    const restaurants = document.querySelectorAll('.restaurant-card');
    restaurants.forEach(restaurant => {
        if (cuisine === 'all' || restaurant.dataset.cuisine === cuisine) {
            restaurant.style.display = 'block';
        } else {
            restaurant.style.display = 'none';
        }
    });
}