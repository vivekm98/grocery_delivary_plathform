const carouselInner = document.getElementById("carousel-inner");
const carouselIndicators = document.getElementById("carousel-indicators");

fetch("http://localhost:8000/api/posters/")  // DRF API endpoint
  .then(res => res.json())
  .then(data => {
    data.forEach((poster, index) => {
      // Carousel item
      const itemDiv = document.createElement("div");
      itemDiv.className = index === 0 ? "carousel-item active" : "carousel-item";
      itemDiv.innerHTML = `
        <img src="${poster.image}" class="d-block w-100 carousel-img" alt="${poster.title || 'Poster'}">
      `;
      carouselInner.appendChild(itemDiv);

      // Indicator button
      const button = document.createElement("button");
      button.type = "button";
      button.setAttribute("data-bs-target", "#bannerCarousel");
      button.setAttribute("data-bs-slide-to", index);
      if (index === 0) button.className = "active";
      carouselIndicators.appendChild(button);
    });
  })
  .catch(err => console.error("Error fetching posters:", err));
