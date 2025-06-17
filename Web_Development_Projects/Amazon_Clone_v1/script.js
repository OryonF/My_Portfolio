/************************************************* 
 * Program Name: Amazon Clone Javascript File
 * Author Name: Oryon James Facey
 * Date: June 17 2025
 * Description: This Javascript script file is to
 * give interactivity to the header slider images
 * on the Amazon site and to allow the product
 * slider images to be scrollable using the mouse
 * wheel.
 ************************************************/

const imgs = document.querySelectorAll('.header-slider ul img');

const prev_btn = document.querySelector('.control_prev');

const next_btn = document.querySelector('.control_next');

let n = 0;

/*
 * Creates a function that iterates through all of 
 * the elements in the imgs array from the const
 * above and hides them by setting it's display to
 * none. Later the img at the index of n is set to
 * block to become visible.
 */

function changeSlide(){

    for (let i = 0; i < imgs.length; i++){

        imgs[i].style.display = 'none';

    }

    imgs[n].style.display = 'block';
}

changeSlide();

/* An add event listener is added to the prev_btn
 * variable so that when you click on the button
 * depending on the index of the imgs array it
 * will go back 1 index if greater than zero or
 * it will go to the last image if the index of
 * imgs is zero.
 */

prev_btn.addEventListener('click', (e)=> {

    if(n > 0){

        n--;

    }else{

        n = imgs.length - 1;

    }

    changeSlide();

})

/* The next button is just like the prev button
 * the different is if the index of imgs is 
 * less than imgs.length - 1 than it will go up
 * one if it is the max index value,
 * imgs.length - 1. It will go back to the first
 * image of the img index.
 */

next_btn.addEventListener('click', (e)=> {

    if(n < imgs.length - 1){

        n++;

    }else{

        n = 0;

    }

    changeSlide();
    
})

/* This code takes away the default useability
 * of the element and than adds an event
 * listener that allows the user to scroll
 * with their mouse wheel.
 */

const scrollContainer = document.querySelectorAll('.products');

for(const item of scrollContainer){

    item.addEventListener('wheel', (evt)=>{

        evt.preventDefault();

        item.scrollLeft += evt.deltaY;

    })

}