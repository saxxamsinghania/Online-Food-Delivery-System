window.onload = function() {
    updateCartDisplay();
};

async function fetchCart() {
    try {
        const response = await fetch('/customer/cart');
        const cart = await response.json();
        return cart
    } catch (error) {
        console.error('Failed to fetch cart:', error);
    }
}

function addToCart(item) {
    fetch(`/customer/add_to_cart/${item.MenuItemID}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            RestaurantID: item.RestaurantID
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCartDisplay();
        }
    });
}

function removeFromCart(itemId) {
    fetch(`/customer/remove_from_cart/${itemId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCartDisplay();
        }
    });
}

function clearCart() {
    fetch('/customer/clear_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',

        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCartDisplay();
        }
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function updateCartDisplay() {
    // Fetch cart items from server
    try {
        const response = await fetch('/customer/cart');
        const cartItems = await response.json();
        const cartSummary = document.getElementById('cartSummary');
        const cartItemsContainer = document.getElementById('cartItems');
        const cartTotal = document.getElementById('cartTotal');
        
        if (cartItems.length === 0) {
            cartSummary.style.display = 'none';
            return;
        }

        cartSummary.style.display = 'block';
        cartItemsContainer.innerHTML = cartItems.map(item => `
            <div class="cart-item">
                <div class="cart-item-details">
                    <span>${item.Name} x ${item.Quantity} - <small style="color:#808080;">${item.restaurant}</small></span>
                </div>
                <div class="cart-item-amount">
                    <span>Rs. ${(item.Price * item.Quantity).toFixed(2)}</span>
                </div>
                <button onclick="removeFromCart(${item.MenuItemID})" class="btn-remove">Remove</button>
            </div>
        `).join('');

        const total = cartItems.reduce((sum, item) => sum + (item.Price * item.Quantity), 0);
        cartTotal.textContent = 'Rs. ' + total.toLocaleString('en-IN', { minimumFractionDigits: 2 });
    } catch (error) {
        console.error('Failed to update cart:', error);
    }
}

async function placeOrder() {
    const restaurantId = document.querySelector('.restaurant-menu').dataset.restaurantId;
    
    try {
        const cart = await fetchCart();
        console.log(cart);
        const response = await fetch('/customer/place-order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                RestaurantID: restaurantId,
                items: cart
            })
        });
        
        const data = await response.json();        
        
        if (data.success) {
            const orderId = data.order_id;
            window.location.href = `/order/${data.order_id}`; 

        } else {
            showAlert(data.error);
        }
    } catch (error) {
        console.log(error);
        showAlert('Failed to place order. Please try again.');
    }
}

async function process_the_Payment(orderId, grand_total) {
    const response = await fetch('/order/generate-qr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            total_amount: grand_total
            
        })
    })
    window.location.href = `/order/process-payment/${orderId}`;
}

document.addEventListener('DOMContentLoaded', function() {
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
    
    const printButton = document.createElement('button');
    printButton.textContent = 'Print Receipt';
    printButton.classList.add('btn', 'btn-secondary');
    printButton.addEventListener('click', function() {
        window.print();
    });
    
    const actionsContainer = document.querySelector('.confirmation-actions');
    if (actionsContainer) {
        actionsContainer.appendChild(printButton);
    }
    
});
