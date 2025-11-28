
const access = localStorage.getItem("access");
if (!access) {
    alert("Please login first!");
    window.location.href = "login.html";
}

/* Modal */
const orderModal = new bootstrap.Modal(document.getElementById('orderModal'));
const deliverySlots = ["Morning", "Afternoon", "Evening"];

/* Load delivery slots */
function loadDeliverySlots() {
    const slotSelect = document.getElementById("slot");
    deliverySlots.forEach(slot => {
        const op = document.createElement("option");
        op.value = slot;
        op.textContent = slot;
        slotSelect.appendChild(op);
    });
}

/* Load cart data */
async function loadCart() {
    const container = document.getElementById("cartContainer");

    const res = await fetch("http://127.0.0.1:8000/api/cart/", {
        headers: { "Authorization": "Bearer " + access }
    });

    const data = await res.json();
    container.innerHTML = "";

    if (data.length === 0) {
        container.innerHTML = `<h5 id="emptyCart">Your cart is empty 🛒</h5>`;
        document.getElementById("orderBtn").style.display = "none";
        return;
    }

    data.forEach(item => {
        const p = item.product;

        container.innerHTML += `
        <div class="cart-card">
            <div>
                <div class="cart-details">
                    <h5>${p.name}</h5>
                    <p>Qty: <span id="qty-${item.id}">${item.quantity}</span> ${p.unit_name}</p>
                    <p class="fw-bold">₹ ${(item.quantity * p.price).toFixed(2)}</p>
                </div>

                <div class="d-flex gap-2 mt-2">
                    <button class="btn btn-minus" onclick="updateQuantity(${item.id}, -1)">−</button>
                    <button class="btn btn-plus" onclick="updateQuantity(${item.id}, 1)">+</button>
                    <button class="btn btn-remove px-3" onclick="removeItem(${item.id})">Remove</button>
                </div>
            </div>

            <img src="${p.image}" alt="${p.name}">
        </div>
        `;
    });
}

/* Update quantity */
async function updateQuantity(cartId, delta) {
    const qtyEl = document.getElementById(`qty-${cartId}`);
    let newQty = parseInt(qtyEl.innerText) + delta;
    if (newQty < 1) return;

    await fetch(`http://127.0.0.1:8000/api/cart/${cartId}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json", "Authorization": "Bearer " + access },
        body: JSON.stringify({ quantity: newQty })
    });

    loadCart();
}

/* Remove item */
async function removeItem(cartId) {
    if (!confirm("Remove this item?")) return;

    await fetch(`http://127.0.0.1:8000/api/cart/${cartId}/`, {
        method: "DELETE",
        headers: { "Authorization": "Bearer " + access }
    });

    loadCart();
}

/* Place Order */
document.getElementById("orderBtn").addEventListener("click", () => {
    orderModal.show();
});

document.getElementById("orderForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const body = {
        first_name: first_name.value,
        last_name: last_name.value,
        phone: phone.value,
        address: address.value,
        slot: slot.value,
    };

    await fetch("http://127.0.0.1:8000/api/orders/", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": "Bearer " + access },
        body: JSON.stringify(body)
    });

    alert("Order placed successfully!");
    orderModal.hide();
    loadCart();
});

/* Logout */
function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

/* Start */
document.addEventListener("DOMContentLoaded", () => {
    loadDeliverySlots();
    loadCart();
});
