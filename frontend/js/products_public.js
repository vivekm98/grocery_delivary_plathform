// products.js
const API_URL = "http://127.0.0.1:8000/api/products/";

document.addEventListener("DOMContentLoaded", () => {
    loadProducts();
    document.getElementById("applyFilters").addEventListener("click", loadProducts);
});

// Load Products with Filters
async function loadProducts() {
    const container = document.getElementById("productContainer");
    container.innerHTML = "<p>Loading products...</p>";

    // Get filter values
    const category = document.getElementById("categoryFilter").value;
    const search = document.getElementById("productSearch").value.trim();
    const minPrice = document.getElementById("minPrice").value.trim();
    const maxPrice = document.getElementById("maxPrice").value.trim();

    // Build query string only if values exist
    let query = [];
    if (category) query.push(`category=${category}`);
    if (search) query.push(`search=${encodeURIComponent(search)}`);
    if (minPrice) query.push(`min_price=${minPrice}`);
    if (maxPrice) query.push(`max_price=${maxPrice}`);

    const url = `${API_URL}${query.length ? "?" + query.join("&") : ""}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        console.log("URL Sent:", url);
        console.log("API Response:", data);

        if (!Array.isArray(data)) {
            container.innerHTML = `<p class="text-danger">Failed to load products. ${data.detail || ""}</p>`;
            return;
        }

        if (data.length === 0) {
            container.innerHTML = "<p>No products found.</p>";
            return;
        }

        container.innerHTML = "";
        data.forEach(product => {
    container.innerHTML += `
    <div class="card p-2 shadow-sm" style="width: 18rem;">
        <img src="${product.image}" class="card-img-top" style="height:180px; object-fit:cover;">
        <div class="card-body">
            <h5 class="card-title">${product.name}</h5>
            <p class="text-muted mb-1"><strong>Unit:</strong> ${product.unit_name}</p>
            <p class="text-muted mb-1"><strong>Category:</strong> ${product.category_name}</p>
            <p class="text-secondary mb-2">${product.description}</p>
            <h6 class="text-success fw-bold">₹${product.price}</h6>
            <button class="btn btn-primary w-100 mt-2" onclick="addToCart(${product.id})">
                Add to Cart 🛒
            </button>
        </div>
    </div>
    `;
});
    } catch (error) {
        console.error("Error fetching products:", error);
        container.innerHTML = `<p class="text-danger">Error loading products. Check console.</p>`;
    }
}

// Add to Cart
async function addToCart(productId) {
    const user = JSON.parse(localStorage.getItem("user"));
    if (!user) {
        alert("Please login first!");
        window.location.href = "login.html";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/api/cart/add/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + user.access
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: 1
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            alert("Error: " + (errData.detail || "Could not add to cart."));
            return;
        }

        alert("Added to cart!");
    } catch (err) {
        console.error("Add to cart failed:", err);
        alert("Something went wrong while adding to cart.");
    }
}