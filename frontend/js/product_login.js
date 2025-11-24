document.addEventListener("DOMContentLoaded", () => {
    loadProducts();

    async function loadProducts() {
        const container = document.getElementById("productContainer");
        container.innerHTML = "Loading products...";

        try {
            const res = await fetch("http://127.0.0.1:8000/api/products/");
            const data = await res.json();

            if (!Array.isArray(data)) {
                container.innerHTML = "Failed to load products.";
                return;
            }

            container.innerHTML = "";
            data.forEach(product => {
                const shortDesc = product.description.length > 60
                    ? product.description.substring(0, 60) + "..."
                    : product.description;

                container.innerHTML += `
                    <div class="card p-2 shadow-sm" style="width: 18rem;">
                        <img src="${product.image}" class="card-img-top" style="height:180px; object-fit:cover;">
                        <div class="card-body">
                            <h5 class="card-title">${product.name}</h5>
                            <p class="text-muted mb-1"><strong>Stock:</strong> ${product.stock} ${product.unit_name}</p>
                            <p class="text-muted mb-1"><strong>Category:</strong> ${product.category_name}</p>
                            <p class="text-secondary mb-2">${shortDesc}</p>
                            <h6 class="text-success fw-bold">₹${product.price}</h6>
                            <button class="btn btn-primary w-100 mt-2" onclick="addToCart(${product.id})">
                                Add to Cart 🛒
                            </button>
                        </div>
                    </div>
                `;
            });

        } catch (err) {
            console.error(err);
            container.innerHTML = "Error loading products.";
        }
    }

    // Expose addToCart globally
    window.addToCart = async function(productId) {
        const access = localStorage.getItem("access");
        if (!access) {
            alert("Please login first!");
            window.location.href = "login.html";
            return;
        }

        try {
            const res = await fetch("http://127.0.0.1:8000/api/cart/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + access
                },
                body: JSON.stringify({ product_id: productId, quantity: 1 })
            });

            const data = await res.json();
            if (!res.ok) {
                alert(data.detail || "Failed to add to cart");
                return;
            }

            alert("Product added to cart!");
        } catch (err) {
            console.error(err);
            alert("Error adding to cart");
        }
    };
});