// Fetch banners from Poster API
async function fetchBanners() {
    try {
        const response = await fetch('http://localhost:8000/api/posters/');
        const banners = await response.json();
        displayBanners(banners);
    } catch (error) {
        console.error('Error fetching banners:', error);
    }
}

function displayBanners(banners) {
    const indicators = document.getElementById('carousel-indicators');
    const inner = document.getElementById('carousel-inner');

    indicators.innerHTML = '';
    inner.innerHTML = '';

    banners.forEach((banner, index) => {
        // Indicators
        const indicator = `
            <button type="button"
                    data-bs-target="#bannerCarousel"
                    data-bs-slide-to="${index}"
                    class="${index === 0 ? 'active' : ''}">
            </button>
        `;
        indicators.innerHTML += indicator;

        // Slider Item
        const item = `
            <div class="carousel-item ${index === 0 ? 'active' : ''}">
                <img src="${banner.image}" class="d-block w-100" alt="Banner">
                <div class="carousel-caption d-none d-md-block">
                    <h5>${banner.title || ''}</h5>
                    <p>${banner.description || ''}</p>
                </div>
            </div>
        `;
        inner.innerHTML += item;
    });
}

// Load banners on page load
fetchBanners();