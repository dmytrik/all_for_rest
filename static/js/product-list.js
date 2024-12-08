const COUNT_OF_PRODUCTS = 9;

let current_page = 1;
const load = document.querySelector(".load");
const loader = document.querySelector(".loader")
const container = document.querySelector(".product-list");
const url = container.getAttribute("data-url");
const form = document.querySelector(".product-search-form");
let search_value = "";

load.addEventListener("click", load_more);
form.addEventListener("submit", search_product);


function search_product(e) {
    e.preventDefault();
    current_page = 1;
    search_value = e.target.name.value;
    get_products(e.target.name.value);
    container.innerHTML = "";
    load.classList.add("hidden");
    loader.classList.remove("hidden");
}

function get_products(name = "") {
    fetch(`${url}?page=${current_page}&name=${name}`).then(res => res.json()).then(res => {
        make_markup(res);
        loader.classList.add("hidden")
    }
    ).catch(
        err => {
            console.clear()
        }
    );
}

function make_markup(products) {
    console.log(products)
    if (products.length < COUNT_OF_PRODUCTS) {
        load.classList.add("hidden")
    }
    if (products.length === 0) {
        container.innerHTML = `<h1 class="section-title" style="text-align: center">Oops nothing found(</h1>`
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

    if (current_page === 1) {
        container.innerHTML = products_markup;
    } else {
        container.insertAdjacentHTML("beforeend", products_markup);
    }

    if (products.length < COUNT_OF_PRODUCTS) {
        load.classList.add("hidden")
    } else {
        load.classList.remove("hidden")
    }
}

function load_more() {
    load.classList.add("hidden")
    loader.classList.remove("hidden")
    current_page += 1;
    get_products(search_value);
}

get_products()
