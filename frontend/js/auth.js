// Show/hide links based on login state
const token = localStorage.getItem("access_token");

if (token) {
  document.getElementById("login-nav").style.display = "none";
  document.getElementById("register-nav").style.display = "none";
  document.getElementById("logout-nav").style.display = "block";
}

// Logout function
function logout() {
  localStorage.removeItem("access_token");
  alert("Logged out successfully!");
  window.location.href = "index.html";
}
