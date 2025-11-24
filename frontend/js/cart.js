// cart.js

// Load cart items from localStorage
function loadCart() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const container = document.getElementById("cartContainer");
  container.innerHTML = "";

  if (cart.length === 0) {
    container.innerHTML = "<p>Your cart is empty.</p>";
    document.getElementById("cartTotal").textContent = "0.00";
    return;
  }

  let total = 0;

  cart.forEach(item => {
    // Fetch product details from API
    fetch(`http://127.0.0.1:8000/api/products/${item.id}/`)
      .then(res => res.json())
      .then(product => {
        const subtotal = product.price * item.quantity;
        total += subtotal;

        const card = document.createElement("div");
        card.classList.add("card", "mb-2");
        card.innerHTML = `
          <div class="card-body d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center">
              <img src="${product.image || 'assets/placeholder.png'}" width="60" class="me-3">
              <div>
                <h6 class="m-0">${product.name}</h6>
                <small>${product.unit_name} | $${product.price.toFixed(2)} each</small>
              </div>
            </div>
            <div class="d-flex align-items-center">
              <input type="number" min="1" value="${item.quantity}" class="form-control form-control-sm me-2 quantity-input" data-id="${item.id}" style="width:70px;">
              <button class="btn btn-sm btn-danger remove-btn" data-id="${item.id}">Remove</button>
            </div>
          </div>
        `;
        container.appendChild(card);

        document.getElementById("cartTotal").textContent = total.toFixed(2);

        // Update quantity
        card.querySelector(".quantity-input").addEventListener("change", e => {
          const qty = parseInt(e.target.value);
          updateCartItem(item.id, qty);
        });

        // Remove item
        card.querySelector(".remove-btn").addEventListener("click", e => {
          removeCartItem(item.id);
        });
      });
  });
}

// Update quantity in localStorage
function updateCartItem(id, quantity) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart = cart.map(item => item.id == id ? { ...item, quantity } : item);
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();
}

// Remove item from cart
function removeCartItem(id) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart = cart.filter(item => item.id != id);
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();
}

// Checkout button
document.getElementById("checkoutBtn").addEventListener("click", () => {
  alert("Checkout not implemented yet!");
});

document.addEventListener("DOMContentLoaded", loadCart);
