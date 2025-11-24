let selectedCategory = "";
let searchQuery = "";
window.filterByCategory = function(categoryId) {
  selectedCategory = categoryId;
  loadProducts();
}

// Function called by category.js when a category is clicked
function filterByCategory(categoryId) {
  selectedCategory = categoryId;
  loadProducts();
}

// Load products from API
async function loadProducts() {
  try {
    let url = `${BASE_URL}/products/`;
    const params = [];
    if (selectedCategory) params.push(`category=${selectedCategory}`);
    if (searchQuery) params.push(`search=${searchQuery}`);
    if (params.length) url += "?" + params.join("&");

    const res = await fetch(url);
    if (!res.ok) throw new Error("Failed to fetch products");

    const products = await res.json();
    renderProducts(products);
  } catch (err) {
    console.error("Error loading products:", err);
  }
}

// Render products to page
function renderProducts(products) {
  const container = document.getElementById("productContainer");
  container.innerHTML = "";

  products.forEach(p => {
    const card = document.createElement("div");
    card.classList.add("product-card", "border", "p-2", "shadow-sm");
    card.style.width = "200px";

    card.innerHTML = `
      <img src="${p.image || 'assets/placeholder.png'}" class="w-100" style="height:150px;object-fit:cover;" alt="${p.name}">
      <h6>${p.name}</h6>
      <p>${p.price.toFixed(2)} RS</p>
      <small> Stock: ${p.stock} ${p.unit_name}</small>
      <p class="product-desc">${p.description || ''}</p>
      <button class="btn btn-sm btn-primary w-100 add-to-cart" data-id="${p.id}">Add to Cart</button>
    `;
    container.appendChild(card);
  });

  // Add-to-cart
  document.querySelectorAll(".add-to-cart").forEach(btn => {
    btn.addEventListener("click", e => {
      const productId = e.target.dataset.id;
      addToCart(productId);
    });
  });
}

// Cart function
function addToCart(productId) {
  const user = JSON.parse(localStorage.getItem("user")); // get logged-in user
  if (!user) {
    // User is not logged in
    alert("You must be logged in to add products to cart!");
    window.location.href = "login.html"; // redirect to login page
    return;
  }

  // User is logged in – proceed to add to cart
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const existing = cart.find(item => item.id == productId);
  if (existing) existing.quantity += 1;
  else cart.push({ id: productId, quantity: 1 });

  localStorage.setItem("cart", JSON.stringify(cart));
  alert("Product added to cart!");
}




// Search products
document.getElementById("productSearch").addEventListener("input", e => {
  searchQuery = e.target.value;
  loadProducts();
});

// Initialize products on page load
document.addEventListener("DOMContentLoaded", () => {
  loadProducts();
});
