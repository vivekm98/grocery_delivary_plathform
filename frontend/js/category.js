// category.js
const BASE_URL = "http://127.0.0.1:8000/api";

async function loadCategories() {
  try {
    const res = await fetch(`${BASE_URL}/categories/`);
    const categories = await res.json();

    const container = document.getElementById("categoryContainer");
    container.innerHTML = ""; // clear previous

    categories.forEach(cat => {
      // Create card div
      const card = document.createElement("div");
      card.classList.add("category-card", "text-dark");
      card.style.cursor = "pointer";

      // Fill inner HTML
      card.innerHTML = `
        <img src="${cat.image || 'assets/placeholder.png'}" class="category-img" alt="${cat.name}">
        <div class="p-2">
          <h6 class="m-0">${cat.name}</h6>
        </div>
      `;

      // Attach click listener to filter products
      card.addEventListener("click", () => {
        window.filterByCategory(cat.id); // calls products.js function
      });

      // Add card to container
      container.appendChild(card);
    });
  } catch (error) {
    console.error("Error loading categories:", error);
  }
}

// Load categories when page loads
document.addEventListener("DOMContentLoaded", loadCategories);
