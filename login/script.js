let signUpBtn = document.querySelector('.signupbtn');
let signInBtn = document.querySelector('.signinbtn');
let title = document.querySelector('.title');
let underline = document.querySelector('.underline');

signInBtn.addEventListener('click',()=>{
    title.innerHTML= 'Sign In';
    signUpBtn.classList.add('disable');
    signUpBtn.classList.remove('disable');
})