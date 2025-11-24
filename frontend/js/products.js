// products.js

// BASE_URL is already declared in category.js
// Do not redeclare it here

async function loadProducts(category = "", search = "") {
  try {
    let url = `${BASE_URL}/products/`;
    const params = [];

    if (category) params.push(`category=${category}`);
    if (search) params.push(`search=${search}`);
    if (params.length) url += "?" + params.join("&");

    const res = await fetch(url);
    if (!res.ok) throw new Error("Failed to fetch products");

    const products = await res.json();

    const container = document.getElementById("productContainer");
    container.innerHTML = ""; // clear previous products

    products.forEach(p => {
      const card = document.createElement("div");
      card.classList.add("product-card");

      card.innerHTML = `
        <img src="${p.image || 'assets/placeholder.png'}" alt="${p.name}">
        <h6>${p.name}</h6>
        <p>$${p.price.toFixed(2)}</p>
        <small>${p.unit_name} | Stock: ${p.stock}</small>
        <p class="product-desc">${p.description || ''}</p>
        <button class="btn btn-sm btn-primary add-to-cart" data-id="${p.id}">Add to Cart</button>
      `;

      container.appendChild(card);
    });

    // Attach Add to Cart event listeners
    document.querySelectorAll(".add-to-cart").forEach(button => {
      button.addEventListener("click", (e) => {
        const productId = e.target.getAttribute("data-id");
        addToCart(productId);
      });
    });

  } catch (error) {
    console.error("Error loading products:", error);
  }
}

// Add to cart function using localStorage
function addToCart(productId) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  const existing = cart.find(item => item.id == productId);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({id: productId, quantity: 1});
  }

  localStorage.setItem("cart", JSON.stringify(cart));
  alert("Product added to cart!");
}

// Load all products on page load
document.addEventListener("DOMContentLoaded", () => {
  loadProducts();
});
