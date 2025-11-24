const BASE_URL = "http://127.0.0.1:8000/api";

async function loadCategories() {
  try {
    const res = await fetch(`${BASE_URL}/categories/`);
    const categories = await res.json();

    let container = document.getElementById("categoryContainer");
    container.innerHTML = "";

    categories.forEach(cat => {
      container.innerHTML += `
        <a href="products.html?category=${cat.id}" class="text-decoration-none text-dark">
          <div class="category-card">
            <img src="${cat.image}" class="category-img">
            <div class="p-2">
              <h6 class="m-0">${cat.name}</h6>
            </div>
          </div>
        </a>
      `;
    });

  } catch (error) {
    console.error("Error loading categories:", error);
  }
}

loadCategories();
