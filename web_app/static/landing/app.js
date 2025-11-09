// Initialize GSAP
gsap.registerPlugin(ScrollTrigger);

// Set default easing
gsap.defaults({ ease: "power2.out" });

// Hero section animations
gsap.timeline()
  .to(".hero-title", { 
    opacity: 1, 
    y: 0, 
    duration: 1,
    ease: "power4.out"
  })
  .to(".hero-subtitle", { 
    opacity: 1, 
    y: 0, 
    duration: 0.8 
  }, "-=0.6")
  .to(".hero-buttons", { 
    opacity: 1, 
    y: 0, 
    duration: 0.8 
  }, "-=0.4")
  .to(".hero-image", { 
    opacity: 1, 
    y: 0, 
    duration: 1 
  }, "-=0.2");

// Section title animations
gsap.utils.toArray(".section-title, .section-subtitle").forEach((element, i) => {
  gsap.from(element, {
    scrollTrigger: {
      trigger: element,
      start: "top 85%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.8
  });
});

// Feature cards animation
gsap.utils.toArray(".feature-card").forEach((card, i) => {
  gsap.from(card, {
    scrollTrigger: {
      trigger: card,
      start: "top 90%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.6,
    delay: i * 0.1
  });
});

// Steps animation
gsap.utils.toArray(".step").forEach((step, i) => {
  gsap.from(step, {
    scrollTrigger: {
      trigger: step,
      start: "top 90%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.6,
    delay: i * 0.2
  });
});

// Testimonial cards animation
gsap.utils.toArray(".testimonial-card").forEach((card, i) => {
  gsap.from(card, {
    scrollTrigger: {
      trigger: card,
      start: "top 90%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.6,
    delay: i * 0.1
  });
});

// Pricing cards animation
gsap.utils.toArray(".pricing-card").forEach((card, i) => {
  gsap.from(card, {
    scrollTrigger: {
      trigger: card,
      start: "top 90%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.6,
    delay: i * 0.2
  });
});

// CTA section animations
gsap.utils.toArray(".cta-content > *").forEach((element, i) => {
  gsap.from(element, {
    scrollTrigger: {
      trigger: element,
      start: "top 90%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 30,
    duration: 0.6,
    delay: i * 0.2
  });
});

// Button hover effects
document.querySelectorAll(".btn").forEach(button => {
  button.addEventListener("mouseenter", () => {
    gsap.to(button, {
      y: -3,
      duration: 0.3
    });
  });
  
  button.addEventListener("mouseleave", () => {
    gsap.to(button, {
      y: 0,
      duration: 0.3
    });
  });
});

// Navbar scroll effect
const updateNavbarBackground = () => {
  const isDarkMode = document.body.classList.contains('dark');
  const bgColor = isDarkMode ? "rgba(45, 38, 33, 0.8)" : "rgba(245, 241, 230, 0.8)";
  
  gsap.to(".header", {
    scrollTrigger: {
      trigger: document.body,
      start: "top top",
      end: "100px top",
      scrub: true
    },
    backgroundColor: bgColor,
    boxShadow: "var(--shadow-sm)",
    duration: 0.1
  });
};

// Initialize navbar background
updateNavbarBackground();

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      gsap.to(window, {
        duration: 1,
        scrollTo: {
          y: target,
          offsetY: 80
        },
        ease: "power2.inOut"
      });
    }
  });
});

// Hamburger menu functionality
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

if (hamburger) {
  hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
    
    // Animate hamburger icon
    const isOpen = navLinks.classList.contains("active");
    const bars = hamburger.querySelectorAll("i");
    
    if (isOpen) {
      gsap.to(bars[0], { rotation: 45, y: 6, duration: 0.3 });
      gsap.to(bars[1], { opacity: 0, duration: 0.3 });
      gsap.to(bars[2], { rotation: -45, y: -6, duration: 0.3 });
    } else {
      gsap.to(bars[0], { rotation: 0, y: 0, duration: 0.3 });
      gsap.to(bars[1], { opacity: 1, duration: 0.3 });
      gsap.to(bars[2], { rotation: 0, y: 0, duration: 0.3 });
    }
  });
}

// Form animations
const formInputs = document.querySelectorAll("input, textarea, select");
formInputs.forEach(input => {
  input.addEventListener("focus", () => {
    gsap.to(input, {
      scale: 1.02,
      duration: 0.2
    });
  });
  
  input.addEventListener("blur", () => {
    gsap.to(input, {
      scale: 1,
      duration: 0.2
    });
  });
});

// Initialize ScrollTrigger refresh on window resize
window.addEventListener("resize", () => {
  ScrollTrigger.refresh();
});

// Theme toggle functionality
const toggleTheme = () => {
  document.body.classList.toggle('dark');
  updateNavbarBackground();
  ScrollTrigger.refresh();
  
  // Update theme toggle button icon
  const themeToggle = document.getElementById('theme-toggle');
  const icon = themeToggle.querySelector('i');
  if (document.body.classList.contains('dark')) {
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
  } else {
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
  }
};

// Document ready
document.addEventListener("DOMContentLoaded", function() {
  // Initialize any additional animations or functionality here
  console.log("Landing page loaded with GSAP animations");
  
  // Add event listener for theme toggle button
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
});