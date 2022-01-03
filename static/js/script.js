// nav fix top 
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) {
            document.getElementById('navbar_top').classList.add('fixed-top');
            // document.getElementById('navbar_top').classList.add('_nav');
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        }
        else{
            // document.getElementById('navbar_top').classList.remove('_nav');
        }
    });
});
