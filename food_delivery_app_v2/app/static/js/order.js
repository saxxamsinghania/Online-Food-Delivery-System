// app/static/js/order.js
async function rateOrder(rating) {
    const orderId = document.querySelector('.order-details').dataset.orderid;
    console.log("ORDER ID: ");
    console.log(orderId);
    try {
        const response = await fetch(`/order/${orderId}/rate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ rating })
        });
        
        const data = await response.json();
        
        if (data.success) {
            const stars = document.querySelectorAll('.star');
            stars.forEach((star, index) => {
                star.textContent = index < rating ? '★' : '☆';
            });
            showAlert('Thank you for your rating!', 'success');
        } else {
            showAlert(data.error);
        }
    } catch (error) {
        showAlert('Failed to submit rating. Please try again.');
    }
}

