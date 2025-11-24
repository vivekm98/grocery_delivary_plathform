document.addEventListener("DOMContentLoaded", () => {
    const user = JSON.parse(localStorage.getItem("user"));
    if (!user) {
        alert("Please login first!");
        window.location.href = "login.html";
        return;
    }

    const container = document.getElementById("cartContainer");
    const cartTotal = document.getElementById("cartTotal");

    async function loadCart() {
        container.innerHTML = "Loading cart...";
        try {
            const res = await fetch("http://127.0.0.1:8000/api/cart/", {
                headers: { "Authorization": "Bearer " + user.access }
            });
            const data = await res.json();

            if (!Array.isArray(data) || data.length === 0) {
                container.innerHTML = "<p>Your cart is empty.</p>";
                cartTotal.innerText = "";
                return;
            }

            container.innerHTML = "";
            let total = 0;

            data.forEach(item => {
                const itemTotal = item.product.price * item.quantity;
                total += itemTotal;

                container.innerHTML += `
                    <div class="card p-3 mb-3 shadow-sm">
                        <div class="d-flex align-items-center">
                            <img src="${item.product.image}" style="height:80px; width:80px; object-fit:cover;" class="me-3">
                            <div class="flex-grow-1">
                                <h5>${item.product.name}</h5>
                                <p class="text-muted mb-1">${item.product.unit_name}</p>
                                <p class="text-success mb-1">₹${item.product.price} × ${item.quantity} = ₹${itemTotal}</p>
                            </div>
                            <div>
                                <input type="number" min="1" value="${item.quantity}" class="form-control mb-2" style="width:80px;" onchange="updateQuantity(${item.id}, this.value)">
                                <button class="btn btn-sm btn-danger w-100" onclick="removeItem(${item.id})">Remove</button>
                            </div>
                        </div>
                    </div>
                `;
            });

            cartTotal.innerText = "Total: ₹" + total;
        } catch (err) {
            console.error(err);
            container.innerHTML = "Error loading cart.";
        }
    }

    window.updateQuantity = async function(cartId, qty) {
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/cart${cartId}/`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + user.access
                },
                body: JSON.stringify({ quantity: qty })
            });
            if (!res.ok) throw new Error("Failed to update quantity");
            loadCart();
        } catch (err) {
            alert(err.message);
        }
    };

    window.removeItem = async function(cartId) {
        if (!confirm("Are you sure you want to remove this item?")) return;
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/cart/${cartId}/`, {
                method: "DELETE",
                headers: { "Authorization": "Bearer " + user.access }
            });
            if (!res.ok) throw new Error("Failed to remove item");
            loadCart();
        } catch (err) {
            alert(err.message);
        }
    };

    // Logout
    document.getElementById("logout-link").addEventListener("click", () => {
        localStorage.clear();
        window.location.href = "login.html";
    });

    loadCart();
});