// app/static/js/menu.js
let cart = [];

// Load cart from localStorage when the page loads
window.onload = function() {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
        cart = JSON.parse(storedCart);
        updateCartDisplay();
    }
};

function addToCart(item) {
    console.log("\nitem\n");
    console.log(item);
    const existingItem = cart.find(i => i.id === item.MenuItemID);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: item.MenuItemID,
            name: item.Name,
            price: item.Price,
            restaurant: item.RestaurantName,
            RestaurantID: item.RestaurantID,
            quantity: 1
        });
    }

    saveCartToLocalStorage();
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartSummary = document.getElementById('cartSummary');
    const cartItems = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');
    
    if (cart.length === 0) {
        cartSummary.style.display = 'none';
        return;
    }
    
    cartSummary.style.display = 'block';
    cartItems.innerHTML = cart.map(item => `
        <div class="cart-item">
            <div class="cart-item-details">
            <span>${item.name} x ${item.quantity} - <small style="color:#808080;">${item.restaurant}</small></span>
            </div>
            <div class= "cart-item-amount">
            <span>Rs. ${(item.price * item.quantity).toFixed(2)}</span>
            </div>
            <button onclick="removeFromCart(${item.id})" class="btn-remove">Remove</button>
        </div>
    `).join('');
    
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    cartTotal.textContent = 'Rs. '+total.toFixed(2);
}

function removeFromCart(itemId) {

    const item = cart.find(item => item.id === itemId);
    if (item) {
        item.quantity -= 1; // Decrease the quantity by 1
        if (item.quantity === 0) {
            cart = cart.filter(item => item.id !== itemId); // Remove item if quantity is 0
        }
    }

    saveCartToLocalStorage();
    updateCartDisplay();
}

function saveCartToLocalStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}
function clearCart() {
    cart = [];

    saveCartToLocalStorage();

    updateCartDisplay();
}


async function placeOrder() {
    const restaurantId = document.querySelector('.restaurant-menu').dataset.restaurantId;
    
    try {
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
            window.location.href = `/order/${data.order_id}`;
        } else {
            showAlert(data.error);
        }
    } catch (error) {
        showAlert('Failed to place order. Please try again.');
    }
}
