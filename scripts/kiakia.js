'use strict'

const menu = document.querySelector('.menu')
const previewLinks = document.querySelector('.preview-links')
const cancel = document.querySelector('.cancel')

menu.addEventListener('click', function(){
   previewLinks.style.display = "grid";
})
cancel.addEventListener('click', function(){
    previewLinks.style.display = "none";
 })