'use strict';


/*-----------------------------------*\
  #PRELOAD
  *
  *loading will be ended after document is loaded
\*-----------------------------------*/

const preloader = document.querySelector("[data-preload]");

window.addEventListener("load",  function(){
    preloader.classList.add("loaded");
    document.body.classList.add("loaded");
});


/**
 * add event listener on multiple elements
 */
const addEventOnElements = function(elements, eventType, callback){
  for(let i = 0, len = elements.length; i < len; i++){
    elements[i].addEventListener(eventType, callback);
  }
}


/**
 * navbar
 */
const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function(){
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);


/**
 * Header & Back To Top BTN
 */
const Header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

let lastScrollPos = 0;

const hideHeader = function (){
  const isScrollBottom = lastScrollPos < window.scrollY;
  const isScrollTop = window.scrollY == lastScrollPos;
  
  if(isScrollBottom){
    Header.classList.add("hide");
    const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function(){
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);
  }else{
    Header.classList.remove("hide");
    const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function(){
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);
  }
  if(isScrollTop || isScrollBottom){
    Header.classList.add("Hault");
    const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function(){
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);
  }else{
    Header.classList.add("Hault");
    const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function(){
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);
  }


  lastScrollPos = window.scrollY;
}

window.addEventListener("scroll", function(){
  if(this.window.scrollY >= 50){
    Header.classList.add("active");
    backTopBtn.classList.add("active");
    hideHeader();
  } else{
    Header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
});



/**
 * hero slider
 */

const heroSlider = document.querySelector("[data-hero-slider]");
const heroSliderItems = document.querySelectorAll("[data-hero-slider-item]");
const heroSliderPrevBtn = document.querySelector("[data-prev-btn]");
const heroSliderNextBtn = document.querySelector("[data-next-btn]");

let currentSlidePos = 0;
let lastActiveSliderItem = heroSliderItems[0];

const updateSliderPos = function(){
  lastActiveSliderItem.classList.remove("active");
  heroSliderItems[currentSlidePos].classList.add("active");
  lastActiveSliderItem = heroSliderItems[currentSlidePos];
}

const slideNext = function(){
  if(currentSlidePos >= heroSliderItems.length - 1){
    currentSlidePos = 0;
  }else{
    currentSlidePos++;
  }

  updateSliderPos();
}

heroSliderNextBtn.addEventListener("click", slideNext);

const slidePrev= function(){
  if(currentSlidePos <= 0){
    currentSlidePos = heroSliderItems.length -1;
  }else{
    currentSlidePos--;
  }

  updateSliderPos();
}

heroSliderPrevBtn.addEventListener("click", slidePrev);

/**
 * auto slide
 */

let autoSlideInterval;

const autoSlide = function(){
  autoSlideInterval = setInterval(function(){
     slideNext();
  }, 7000);
}

addEventOnElements([heroSliderNextBtn, heroSliderPrevBtn], "mouseover", function(){
  clearInterval(autoSlideInterval);
});

addEventOnElements([heroSliderNextBtn, heroSliderPrevBtn], "mouseout", autoSlide);

window.addEventListener("load", autoSlide);

/***
 * parallax effect
 */
const parallaxItems = document.querySelectorAll("[data-parallax-item]");

let x, y;

window.addEventListener("mousemove", function(event){
  x = (event.clientX / window.innerWidth * 10) - 5;
  y = (event.clientY / window.innerHeight * 10) - 5;

  //reverse the number eg. 20 -> -20
  x = x - (x * 2);
  y = y - (y * 2);

  for (let i = 0, len =parallaxItems.length; i < len; i++){
    x = x * Number(parallaxItems[i].dataset.parallaxSpeed);
    y = y * Number(parallaxItems[i].dataset.parallaxSpeed);
    parallaxItems[i].style.transform = `translate3d(${x}px, ${y}px, 0px)`;
  }
});