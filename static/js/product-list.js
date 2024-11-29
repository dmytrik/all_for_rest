let current_page = 1;
const load = document.querySelector(".load");
const container = document.querySelector(".product-list");
const url = container.getAttribute("data-url");

load.addEventListener("click", load_more)

function get_products() {
    fetch(`${url}?page=${current_page}`).then(res => res.json()).then(make_markup);
}

function make_markup(products) {
    console.log(products)
    if (products.length === 0) {
        load.classList.add("hidden")
        return
    }

    const products_markup = products.map(el =>
        `<li class="product-item">
            <div class="img-container">
              <img src="${el.photo}" alt="photo" class = "product-img">
            </div>
            <div class="info-container">
              <p class="product-info" style="color: darkorange">${el.name}</p>
              <p class="product-info">${el.price} грн</p>
              <p class="product-info">${el.type}</p>
              <a href="${el.id}/" class="product-info product-link-info" style="color: darkolivegreen">More info...</a>
            </div>
        </li>`
    ).join("");

    container.insertAdjacentHTML("beforeend", products_markup);

    load.classList.remove("hidden")
}

function load_more() {
    load.classList.add("hidden")
    current_page += 1;
    get_products();
}

get_products()
