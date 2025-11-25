
document.addEventListener("DOMContentLoaded", () => {
    let allProducts = [];
    loadProducts();

    async function loadProducts() {
        const container = document.getElementById("productContainer");
        container.innerHTML = "Loading products...";

        try {
            const res = await fetch("http://127.0.0.1:8000/api/products/");
            if (!res.ok) throw new Error("Failed to fetch products");

            const data = await res.json();
            if (!Array.isArray(data)) {
                container.innerHTML = "Failed to load products.";
                return;
            }

            allProducts = data;
            populateCategories();
            renderProducts(allProducts);
        } catch (err) {
            console.error(err);
            container.innerHTML = "Error loading products.";
        }
    }

    function renderProducts(products) {
        const container = document.getElementById("productContainer");
        container.innerHTML = "";
        products.forEach(product => {
            const shortDesc = product.description.length > 60
                ? product.description.substring(0, 60) + "..."
                : product.description;

            container.innerHTML += `
                <div class="card p-2 shadow-sm m-2" style="width: 18rem;">
                    <img src="${product.image}" class="card-img-top" style="height:180px; object-fit:cover;">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="text-muted mb-1"><strong>Unit:</strong> ${product.unit_name}</p>
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
    }

    function populateCategories() {
        const categorySelect = document.getElementById("categoryFilter");
        const categories = [...new Set(allProducts.map(p => p.category_name))];
        categorySelect.innerHTML = `<option value="">All Categories</option>` +
            categories.map(cat => `<option value="${cat}">${cat}</option>`).join("");
    }

    function applyFilters() {
        const category = document.getElementById("categoryFilter").value;
        const search = document.getElementById("productSearch").value.toLowerCase();
        const minPrice = parseFloat(document.getElementById("minPrice").value) || 0;
        const maxPrice = parseFloat(document.getElementById("maxPrice").value) || Infinity;

        const filtered = allProducts.filter(product => {
            return (
                (category === "" || product.category_name === category) &&
                product.name.toLowerCase().includes(search) &&
                product.price >= minPrice &&
                product.price <= maxPrice
            );
        });

        renderProducts(filtered);
    }

    // Live filter events
    document.getElementById("categoryFilter").addEventListener("change", applyFilters);
    document.getElementById("productSearch").addEventListener("input", applyFilters);
    document.getElementById("minPrice").addEventListener("input", applyFilters);
    document.getElementById("maxPrice").addEventListener("input", applyFilters);

    // Add product to cart
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