const csrftoken = document.querySelector('[name=csrf-token]').content;

// Ürün silme
document.querySelectorAll(".remove-item-btn").forEach(button => {
    button.addEventListener("click", function () {
        const productId = this.dataset.productId;
        const url = this.dataset.url;

        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector(`#cart-item-${productId}`).remove();
                document.querySelector("#cart-total").textContent = `Toplam: ${data.cart_total}`;
            } else {
                alert("Ürün silinemedi!");
            }
        });
    });
});

//adet güncelleme
document.querySelectorAll(".cart-item-quantity").forEach(input => {
    input.addEventListener("change", function () {
        const productId = this.dataset.productId;
        const quantity = this.value;
        const url = this.dataset.url;

        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        }).then(response => response.json())
          .then(data => {
              if (data.success) {
                  // Ürüne ait toplam fiyatı güncelle
                  const productTotal = document.querySelector(`.product-total[data-product-id='${productId}']`);
                  productTotal.textContent = `${data.product_total}`;

                  // Genel toplamı güncelle
                  document.querySelector(".cart-summary h2").textContent = `Toplam: ${data.cart_total}₺`;
              }
          });
    });
});

//sipariş tamamlama

document.querySelector(".complete-order-btn").addEventListener("click", function () {
    const url = this.dataset.url;

    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Siparişiniz tamamlandı!");
            window.location.reload();
        } else {
            alert("Sipariş tamamlanamadı!");
        }
    });
});

