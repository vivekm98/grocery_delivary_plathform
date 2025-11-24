//// category.js
//const CATEGORY_API = "http://127.0.0.1:8000/api/categories/";
//
//document.addEventListener("DOMContentLoaded", loadCategories);
//
//async function loadCategories() {
//    const select = document.getElementById("categoryFilter");
//
//    try {
//        const res = await fetch(CATEGORY_API);
//        const categories = await res.json();
//
//        // Clear existing options
//        select.innerHTML = `<option value="">All Categories</option>`;
//
//        categories.forEach(cat => {
//            const option = document.createElement("option");
//            option.value = cat.id;       // Use ID for backend filter
//            option.textContent = cat.name;
//            select.appendChild(option);
//        });
//    } catch (err) {
//        console.error("Failed to load categories:", err);
//        select.innerHTML = `<option value="">All Categories</option>`;
//    }
//}