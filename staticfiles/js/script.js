// Menü İkonu ve Yan Menü Seçiciler
const menuIcon = document.querySelector('.menu-icon');
const sideMenu = document.querySelector('.side-menu');
const menuItems = document.querySelectorAll('.menu-item');

// Menü İkonuna Tıklayınca Yan Menü Göster/Gizle
menuIcon.addEventListener('click', () => {
    sideMenu.classList.toggle('open');
});

// Menü Öğelerine Tıklayınca Alt Menüleri Göster/Gizle
menuItems.forEach(item => {
    item.addEventListener('click', () => {
        const parent = item.parentElement;
        parent.classList.toggle('open');
    });
});
