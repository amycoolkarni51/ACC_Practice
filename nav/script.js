const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');



registerLink.addEventListener('click',()=> {
  wrapper.classList.add('active');
});

loginLink.addEventListener('click',()=> {
  wrapper.classList.remove('active');
});

btnPopup.addEventListener('click',()=> {
  wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click',()=> {
  wrapper.classList.remove('active-popup');
});


// <div class="form-box register">
//   <h2>Registion</h2>
//   <form action="#">
//     <div class="input-box">
//       <span class="icon">
//         <ion-icon name="person"></ion-icon>
//       </span>
//       <input type="text" required>
//       <label>Username</label>
//     </div>
//     <div class="input-box">
//       <span class="icon">
//         <ion-icon name="mail"></ion-icon>
//       </span>
//       <input type="email" required>
//       <label>Email</label>
//     </div>
//     <div class="input-box">
//       <span class="icon">
//         <ion-icon name="lock-closed"></ion-icon>
//       </span>
//       <input type="password" required>
//       <label>Password</label>
//     </div>
//     <div class="remember-forgot">
//       <label><input type="checkbox">
//         agree to the tems & conditions</label>
//     </div>
//     <button type="submit" class="btn">Register</button>
//     <div class="login-register">
//       <p>Already have an account?<a href="#" class="login-link">Login</a></p>
//     </div>
//   </form>
// </div>
